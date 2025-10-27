"""
Pytest configuration for Module-DeckleOptimiser Integration Tests
This file sets up fixtures and configuration for testing the actual API endpoints
"""
import pytest
import os
from unittest.mock import Mock, patch
import requests
from datetime import datetime

# Test configuration
BASE_URL = os.getenv('API_BASE_URL', 'https://trim-manager.appliedbellcurve.com')
API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))

# Check if we're testing against local application
LOCAL_APP = os.path.exists('application.py')

@pytest.fixture(scope="session")
def api_base_url():
    """Base URL for the Module-DeckleOptimiser API"""
    return BASE_URL

@pytest.fixture(scope="session")
def api_timeout():
    """Timeout for API requests"""
    return API_TIMEOUT

@pytest.fixture(scope="session")
def local_app_available():
    """Check if local application is available"""
    return LOCAL_APP

@pytest.fixture(scope="session", autouse=True)
def verify_hosted_api_connection():
    """Verify connection to hosted Module-DeckleOptimiser API"""
    print(f"Testing connection to hosted API: {BASE_URL}")
    
    try:
        response = requests.get(f"{BASE_URL}/", timeout=10)
        if response.status_code == 200:
            print("Hosted API is accessible and responding")
            print(f"   Response: {response.text.strip()}")
        else:
            print(f"Hosted API responded with status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f" Could not connect to hosted API: {e}")
        print("   Make sure the API is accessible at the configured URL")
    
    yield

@pytest.fixture
def test_headers():
    """Default headers for API requests"""
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

@pytest.fixture
def sample_company():
    """Sample company for testing"""
    return "TEST_COMPANY"

@pytest.fixture
def sample_plant():
    """Sample plant for testing"""
    return "TEST_PLANT"

@pytest.fixture
def sample_machine_type():
    """Sample machine type for testing"""
    return "Primary"

@pytest.fixture
def sample_product_type():
    """Sample product type for testing"""
    return "PROD1"

@pytest.fixture
def sample_product_config():
    """Sample product configuration for testing"""
    return "CONFIG1"

@pytest.fixture
def sample_user_id():
    """Sample user ID for testing"""
    return "test-user-123"

@pytest.fixture
def sample_campaign_id():
    """Sample campaign ID for testing"""
    return "test-campaign-456"

@pytest.fixture
def sample_month_year():
    """Sample month-year for testing"""
    return "2024-01"

@pytest.fixture
def sample_optimization_data():
    """Sample optimization data for testing"""
    return {
        "max_width": 2000,
        "minimum_trim": 50,
        "data": [
            {"width": 1000, "quantity": 10},
            {"width": 1200, "quantity": 15}
        ]
    }

@pytest.fixture
def sample_scheduler_data():
    """Sample scheduler data for testing"""
    return {
        "client_name": "TEST_CLIENT",
        "data": {
            "orders": [
                {"id": 1, "width": 1000, "quantity": 10},
                {"id": 2, "width": 1200, "quantity": 15}
            ],
            "campaign_blocks": {
                "block1": {"start": "2024-01-01", "end": "2024-01-31"}
            }
        }
    }

@pytest.fixture
def sample_planner_data():
    """Sample planner data for testing"""
    return {
        "monthYear": "2024-01",
        "plant": "TEST_PLANT",
        "data": [
            {"material_group": "MET", "quantity": 100},
            {"material_group": "AL", "quantity": 150}
        ]
    }

@pytest.fixture
def sample_campaign_plan():
    """Sample campaign plan for testing"""
    return {
        "client_name": "TEST_CLIENT",
        "campaign_plan": [
            {"material_group": "MET", "line": "Line1", "quantity": 100},
            {"material_group": "AL", "line": "Line2", "quantity": 150}
        ]
    }

@pytest.fixture
def sample_user_data():
    """Sample user data for testing"""
    return {
        "userId": "test-user-123",
        "company": "TEST_COMPANY",
        "email": "test@example.com",
        "machine_type": ["Primary", "Secondary"]
    }

@pytest.fixture
def sample_machine_config():
    """Sample machine configuration for testing"""
    return {
        "machineCategory": "Primary",
        "maxArms": 10,
        "minArms": 2,
        "config": {
            "width_range": [500, 2000],
            "trim_range": [10, 100]
        }
    }

@pytest.fixture
def sample_file_data():
    """Sample file data for testing"""
    return {
        "filename": "test_orders.xlsx",
        "content_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    }

@pytest.fixture
def sample_sales_forecast():
    """Sample sales forecast data for testing"""
    return {
        "client_name": "TEST_CLIENT",
        "month": "2024-01",
        "plant": "TEST_PLANT",
        "forecast": [
            {"group": "MET", "exportQty": 100, "domesticQty": 50},
            {"group": "AL", "exportQty": 150, "domesticQty": 75}
        ]
    }

@pytest.fixture
def sample_slitting_orders():
    """Sample slitting orders data for testing"""
    return {
        "company": "TEST_COMPANY",
        "material_group": "MET",
        "material_codes": ["MAT001", "MAT002"],
        "slitting_orders": {
            "order1": {"width": 1000, "quantity": 10},
            "order2": {"width": 1200, "quantity": 15}
        },
        "start_time": "2024-01-01T00:00:00Z",
        "end_time": "2024-01-31T23:59:59Z",
        "quantity": 1000
    }

@pytest.fixture
def sample_secondary_data():
    """Sample secondary data for testing"""
    return {
        "secondary_data": [
            {"merged_width": 1000, "Sets": 10},
            {"merged_width": 1200, "Sets": 15}
        ],
        "customer_data": [
            {"customer": "CUST1", "quantity": 100},
            {"customer": "CUST2", "quantity": 150}
        ],
        "jumbo_width": 2000,
        "lengthMultiple": 5
    }

@pytest.fixture
def sample_sap_data():
    """Sample SAP data for testing"""
    return {
        "start_date": "2024-01-01",
        "end_date": "2024-01-31",
        "material_code": "MAT001"
    }

@pytest.fixture
def mock_requests():
    """Mock requests for testing error scenarios"""
    with patch('requests.get') as mock_get, \
         patch('requests.post') as mock_post, \
         patch('requests.put') as mock_put, \
         patch('requests.delete') as mock_delete:
        
        # Configure default successful responses
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_response.content = b'{"success": true}'
        mock_response.headers = {'Content-Type': 'application/json'}
        
        mock_get.return_value = mock_response
        mock_post.return_value = mock_response
        mock_put.return_value = mock_response
        mock_delete.return_value = mock_response
        
        yield {
            'get': mock_get,
            'post': mock_post,
            'put': mock_put,
            'delete': mock_delete
        }

@pytest.fixture
def api_client():
    """HTTP client for making API requests"""
    return requests.Session()

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup test environment before each test"""
    # Set test environment variables
    os.environ['TESTING'] = 'true'
    os.environ['API_BASE_URL'] = BASE_URL
    
    yield
    
    # Cleanup after test
    if 'TESTING' in os.environ:
        del os.environ['TESTING']

def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )
    config.addinivalue_line(
        "markers", "api: mark test as API test"
    )

def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers"""
    for item in items:
        # Add integration marker to all tests
        item.add_marker(pytest.mark.integration)
        
        # Add API marker to tests that make HTTP requests
        if any(keyword in item.name.lower() for keyword in ['api', 'endpoint', 'http']):
            item.add_marker(pytest.mark.api)
        
        # Add slow marker to tests that might take longer
        if any(keyword in item.name.lower() for keyword in ['complex', 'large', 'batch']):
            item.add_marker(pytest.mark.slow)