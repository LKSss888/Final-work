import subprocess
import sys
from dotenv import load_dotenv

def run_tests(test_type):
    load_dotenv()
    
    test_commands = {
        "ui": ["pytest", "-m", "ui", "-v", "-s", "--alluredir=./allure-results"],
        "api": ["pytest", "-m", "api", "-v", "--alluredir=./allure-results"],
        "api_mock": ["pytest", "tests/test_api_mock.py", "-v", "--alluredir=./alluredir=./allure-results"],
        "all": ["pytest", "-v", "-s", "--alluredir=./allure-results"]
    }
    
    if test_type not in test_commands:
        print("❌ Неверный тип тестов. Используйте: ui, api, api_mock, all")
        sys.exit(1)
    
    result = subprocess.run(test_commands[test_type], check=False)
    sys.exit(result.returncode)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python run_tests.py [ui|api|api_mock|all]")
        sys.exit(1)
    run_tests(sys.argv[1].lower())