from prefect import flow, task, get_run_logger
from datetime import timedelta
import random
import time

@task(name="Validate Datalake")
def validate_datalake():
    logger = get_run_logger()
    logger.info("✅ Starting Datalake validation...")
    
    # Simulate validation work
    time.sleep(random.uniform(1, 3))
    
    # Simulate results
    tests_run = 12
    failures = 0 if random.random() > 0.1 else 1  # 10% chance of failure
    
    result = {
        "layer": "Datalake",
        "status": "PASS" if failures == 0 else "FAIL",
        "tests_run": tests_run,
        "failures": failures,
        "duration": round(random.uniform(10, 20), 1)
    }
    
    if failures > 0:
        logger.warning(f"⚠️ Found {failures} failures in Datalake validation")
    else:
        logger.info("✅ Datalake validation PASSED")
    
    return result

@task(name="Validate EDW")
def validate_edw(datalake_result: dict):
    logger = get_run_logger()
    logger.info("✅ Starting EDW validation...")
    
    time.sleep(random.uniform(2, 4))
    
    tests_run = 18
    failures = 0 if random.random() > 0.05 else 1  # 5% chance of failure
    
    result = {
        "layer": "EDW",
        "status": "PASS" if failures == 0 else "FAIL",
        "tests_run": tests_run,
        "failures": failures,
        "duration": round(random.uniform(15, 30), 1)
    }
    
    logger.info(f"✅ EDW validation {'PASSED' if failures == 0 else 'FAILED'}")
    return result

@task(name="Validate Datamart")
def validate_datamart(edw_result: dict):
    logger = get_run_logger()
    logger.info("✅ Starting Datamart validation...")
    
    time.sleep(random.uniform(0.5, 2))
    
    tests_run = 8
    failures = 0 if random.random() > 0.15 else 1  # 15% chance of failure
    
    result = {
        "layer": "Datamart",
        "status": "PASS" if failures == 0 else "FAIL",
        "tests_run": tests_run,
        "failures": failures,
        "duration": round(random.uniform(5, 15), 1)
    }
    
    if failures > 0:
        logger.warning("⚠️ Datamart validation found tolerance violations")
    else:
        logger.info("✅ Datamart validation PASSED")
    
    return result

@task(name="Validate Reporting")
def validate_reporting(datamart_result: dict):
    logger = get_run_logger()
    logger.info("✅ Starting Reporting (QlikSense) validation...")
    
    time.sleep(random.uniform(0.5, 1.5))
    
    tests_run = 5
    failures = 0
    
    result = {
        "layer": "Reporting",
        "status": "PASS",
        "tests_run": tests_run,
        "failures": failures,
        "duration": round(random.uniform(2, 5), 1)
    }
    
    logger.info("✅ Reporting validation PASSED")
    return result

@flow(name="EDAG Full Validation Pipeline", log_prints=True)
def edag_validation_flow():
    logger = get_run_logger()
    logger.info("🚀 Starting EDAG Full Validation Pipeline")
    
    # Run validations sequentially
    dl_result = validate_datalake()
    edw_result = validate_edw(dl_result)
    dm_result = validate_datamart(edw_result)
    rep_result = validate_reporting(dm_result)
    
    # Collect results
    results = [dl_result, edw_result, dm_result, rep_result]
    total_tests = sum(r["tests_run"] for r in results)
    total_failures = sum(r["failures"] for r in results)
    avg_duration = sum(r["duration"] for r in results) / len(results)
    
    # Final summary
    overall_status = "PASS" if total_failures == 0 else "FAIL"
    
    logger.info(f"🎉 Pipeline Completed!")
    logger.info(f"📊 Total Tests: {total_tests}")
    logger.info(f"❌ Total Failures: {total_failures}")
    logger.info(f"⏱️ Avg Duration: {avg_duration:.1f}s")
    logger.info(f"✅ Overall Status: {overall_status}")
    
    return {
        "status": overall_status,
        "total_tests": total_tests,
        "total_failures": total_failures,
        "avg_duration": avg_duration,
        "layer_results": results
    }

if __name__ == "__main__":
    # Run the flow
    result = edag_validation_flow()
    print(f"\nFinal Result: {result['status']}")
    print(f"Total Tests: {result['total_tests']}")
    print(f"Total Failures: {result['total_failures']}")