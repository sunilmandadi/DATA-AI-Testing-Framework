from autogen import ConversableAgent, GroupChat, GroupChatManager
import argparse
import os

# Configure local LLM
llm_config = {
    "config_list": [
        {
            "model": "llama3",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama"
        }
    ],
    "temperature": 0.2,
}

def run_validation_task(task_description: str):
    print(f"🧠 Starting multi-agent validation: '{task_description}'")

    # Create agents
    orchestrator = ConversableAgent(
        "Orchestrator",
        system_message="You are the validation commander. Coordinate Datalake→EDW→Datamart→Reporting. Summarize results. Say TERMINATE when done.",
        llm_config=llm_config,
        is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
    )

    datalake_agent = ConversableAgent(
        "Datalake_Agent",
        system_message="You validate raw data in Hadoop/Hive. Check schema, nulls, counts. Use RAG to read specs. Report issues.",
        llm_config=llm_config
    )

    edw_agent = ConversableAgent(
        "EDW_Agent",
        system_message="You validate Teradata EDW. Check SCD2, FKs, aggregations. Reconcile with Datalake. Report discrepancies.",
        llm_config=llm_config
    )

    datamart_agent = ConversableAgent(
        "Datamart_Agent",
        system_message="You validate aggregated datamarts. Check metrics, joins, performance. Use tolerance engine. Flag outliers.",
        llm_config=llm_config
    )

    reporting_agent = ConversableAgent(
        "Reporting_Agent",
        system_message="You validate QlikSense dashboards. Check totals, filters, security. Call Qlik API. Validate visual accuracy.",
        llm_config=llm_config
    )

    # Setup group chat
    groupchat = GroupChat(
        agents=[orchestrator, datalake_agent, edw_agent, datamart_agent, reporting_agent],
        messages=[],
        max_round=20,
        speaker_selection_method="round_robin"
    )
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    # Start conversation
    orchestrator.initiate_chat(manager, message=task_description)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run multi-agent validation")
    parser.add_argument("--task", type=str, required=True, help="Validation task description")
    args = parser.parse_args()
    run_validation_task(args.task)