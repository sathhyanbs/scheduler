import subprocess
import schedule
import time

def run_jmeter_test(test_plan_path, jmeter_path):
    command = f"{jmeter_path} -n -t {test_plan_path}"
    try:
        subprocess.run(command, shell=True, check=True)
        print("JMeter test execution completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"JMeter test execution failed. Error: {e}")

test_plan_path = "AMD\AMD.jmx" 
jmeter_path = "C:/Sathhyan/AIW/apache-jmeter-5.5/bin/jmeter.bat"
# run_jmeter_test(test_plan_path, jmeter_path)

# schedule.every().day.at("08:00").do(run_jmeter_test)
# schedule.every(10).minutes.do(run_jmeter_test, test_plan_path, jmeter_path)
schedule.every().day.at("11:10").do(run_jmeter_test, test_plan_path, jmeter_path)

while True:
    schedule.run_pending()
    time.sleep(1)