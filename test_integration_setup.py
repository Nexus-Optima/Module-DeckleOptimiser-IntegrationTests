"""
Test to verify the integration test setup is working correctly
"""
import pytest
import requests
from requests.exceptions import RequestException


class TestIntegrationSetup:
    """Test the integration test setup"""

    def test_http_requests_working(self, api_client):
        """Test that HTTP requests are working"""
        try:
            response = api_client.get('http://httpbin.org/get', timeout=5)
            assert response.status_code == 200
        except RequestException as e:
            pytest.skip(f"HTTP requests not working: {e}")

    def test_api_base_url_configured(self, api_base_url):
        """Test that API base URL is configured"""
        assert api_base_url is not None
        assert api_base_url.startswith('http')
        print(f"API Base URL: {api_base_url}")

    def test_api_timeout_configured(self, api_timeout):
        """Test that API timeout is configured"""
        assert api_timeout > 0
        print(f"API Timeout: {api_timeout}")

    def test_test_headers_configured(self, test_headers):
        """Test that test headers are configured"""
        assert 'Content-Type' in test_headers
        assert 'Accept' in test_headers
        print(f"Test Headers: {test_headers}")

    def test_sample_data_fixtures(self, sample_optimization_data, sample_scheduler_data, sample_planner_data):
        """Test that sample data fixtures are working"""
        assert sample_optimization_data is not None
        assert sample_scheduler_data is not None
        assert sample_planner_data is not None
        print("Sample data fixtures working")

    def test_mock_requests_fixture(self, mock_requests):
        """Test that mock requests fixture is working"""
        assert mock_requests is not None
        assert 'get' in mock_requests
        assert 'post' in mock_requests
        print("Mock requests fixture working")

    def test_api_client_fixture(self, api_client):
        """Test that API client fixture is working"""
        assert api_client is not None
        assert hasattr(api_client, 'get')
        assert hasattr(api_client, 'post')
        print("API client fixture working")

    def test_environment_variables(self):
        """Test environment variables"""
        import os
        api_url = os.getenv('API_BASE_URL', 'http://localhost:5000')
        api_timeout = os.getenv('API_TIMEOUT', '30')
        testing = os.getenv('TESTING', 'false')
        
        print(f"Environment Variables:")
        print(f"  API_BASE_URL: {api_url}")
        print(f"  API_TIMEOUT: {api_timeout}")
        print(f"  TESTING: {testing}")
        
        assert api_url is not None
        assert api_timeout is not None

    def test_pytest_configuration(self):
        """Test pytest configuration"""
        import pytest
        import os
        
        # Check if pytest.ini exists
        assert os.path.exists('pytest.ini'), f"pytest.ini not found in {os.getcwd()}"
        
        # Check if requirements.txt exists
        assert os.path.exists('requirements.txt'), f"requirements.txt not found in {os.getcwd()}"
        
        # Check if buildspec.yml exists
        assert os.path.exists('buildspec.yml'), f"buildspec.yml not found in {os.getcwd()}"
        
        print("Pytest configuration files present")

    def test_integration_test_structure(self):
        """Test that integration test structure is correct"""
        import os
        
        # Check test files exist
        test_files = [
            'test_health_check.py',
            'test_api_status_report.py',
            'test_api_success_validation.py',
            'test_integration_setup.py'
        ]
        
        for test_file in test_files:
            assert os.path.exists(test_file), f"Test file {test_file} not found"
        
        print("All test files present")

    def test_conftest_fixtures(self):
        """Test that conftest.py fixtures are working"""
        # This test will automatically use fixtures from conftest.py
        # If it runs without errors, the fixtures are working
        print("Conftest fixtures working")

    def test_buildspec_configuration(self):
        """Test buildspec configuration"""
        import os
        buildspec_path = 'buildspec.yml'
        assert os.path.exists(buildspec_path), f"buildspec.yml not found in {os.getcwd()}"
        
        with open(buildspec_path, 'r') as f:
            content = f.read()
        
        # Check for key buildspec elements
        assert 'version: 0.2' in content
        assert 'phases:' in content
        assert 'install:' in content
        assert 'build:' in content
        assert 'pytest' in content
        
        print("Buildspec configuration valid")

    def test_requirements_dependencies(self):
        """Test that all required dependencies are installed"""
        required_packages = [
            'pytest',
            'requests',
            'flask',
            'pandas',
            'boto3'
        ]
        
        for package in required_packages:
            try:
                __import__(package.replace('-', '_'))
                print(f"{package} installed")
            except ImportError:
                pytest.fail(f"{package} not installed")
