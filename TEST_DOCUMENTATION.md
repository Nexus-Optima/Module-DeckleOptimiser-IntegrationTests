# Module-DeckleOptimiser Integration Tests Documentation

## Table of Contents
1. [Overview](#overview)
2. [Test Suite Structure](#test-suite-structure)
3. [Test Files](#test-files)
4. [API Endpoints Tested](#api-endpoints-tested)
5. [Test Configuration](#test-configuration)
6. [Running Tests](#running-tests)
7. [Test Results](#test-results)
8. [CI/CD Integration](#cicd-integration)
9. [Environment Variables](#environment-variables)
10. [Troubleshooting](#troubleshooting)

---

## Overview

This integration test suite validates the Module-DeckleOptimiser API endpoints by making actual HTTP requests to the hosted API. The tests are designed to:

- Verify API endpoints are accessible and responding
- Validate endpoint functionality and error handling
- Ensure proper HTTP status codes and response formats
- Test API connectivity and performance
- Generate comprehensive test reports for CI/CD pipelines

**API Base URL**: `https://trim-manager.appliedbellcurve.com`

**Test Approach**: Integration tests make real HTTP calls to the hosted API, treating responses with status codes 200, 400, and 500 as successful (indicating the endpoint is accessible and responding).

---

## Test Suite Structure

```
Module-DeckleOptimiser-IntegrationTests/
├── buildspec.yml                 # AWS CodeBuild configuration
├── conftest.py                   # Pytest fixtures and configuration
├── config.py                    # Configuration settings
├── pytest.ini                   # Pytest configuration
├── requirements.txt             # Python dependencies
├── setup_env.sh                 # Environment setup script
├── test_health_check.py         # Health check endpoint tests
├── test_api_status_report.py    # Comprehensive API status report
├── test_api_success_validation.py # API accessibility validation
└── test_integration_setup.py     # Test setup verification
```

---

## Test Files

### 1. `test_health_check.py`
**Purpose**: Comprehensive testing of the root health check endpoint (`/`)

**Test Cases**:
- `test_health_check_success` - Validates successful health check response
- `test_health_check_error_handling` - Tests error handling scenarios
- `test_health_check_with_different_methods` - Tests GET, POST, PUT, DELETE methods
- `test_health_check_response_time` - Validates response time performance
- `test_health_check_content_type` - Verifies correct content type headers
- `test_health_check_cors_headers` - Validates CORS headers
- `test_health_check_load` - Tests load handling with multiple requests
- `test_health_check_with_parameters` - Tests endpoint with query parameters
- `test_health_check_authentication` - Validates authentication headers

**Total Tests**: 9

---

### 2. `test_api_status_report.py`
**Purpose**: Comprehensive status report for all API endpoints with detailed output

**Test Cases**:
- `test_api_connectivity` - Validates basic API connectivity
- `test_health_check_endpoints` - Tests health check endpoints
- `test_optimization_endpoints` - Tests optimization API endpoints
- `test_data_fetching_endpoints` - Tests data retrieval endpoints
- `test_scheduler_endpoints` - Tests scheduler API endpoints
- `test_planner_endpoints` - Tests planner API endpoints
- `test_campaign_management_endpoints` - Tests campaign management APIs
- `test_user_machine_endpoints` - Tests user and machine management APIs
- `test_file_processing_endpoints` - Tests file upload and processing endpoints
- `test_additional_endpoints` - Tests additional utility endpoints
- `test_api_summary` - Generates summary report of all endpoints

**Total Tests**: 11

**Features**:
- Detailed status reporting for each endpoint
- Response code validation
- Error message capture
- Endpoint categorization

---

### 3. `test_api_success_validation.py`
**Purpose**: Validates that all API endpoints are accessible and responding

**Test Cases**:
- `test_health_check_success` - Validates health check endpoint
- `test_optimization_endpoints_success` - Validates optimization endpoints accessibility
- `test_data_fetching_endpoints_success` - Validates data fetching endpoints
- `test_scheduler_endpoints_success` - Validates scheduler endpoints
- `test_planner_endpoints_success` - Validates planner endpoints
- `test_campaign_management_endpoints_success` - Validates campaign endpoints
- `test_user_machine_endpoints_success` - Validates user/machine endpoints
- `test_file_processing_endpoints_success` - Validates file processing endpoints
- `test_additional_endpoints_success` - Validates additional endpoints
- `test_all_endpoints_accessible` - Comprehensive endpoint accessibility check

**Total Tests**: 10

**Success Criteria**: Treats status codes 200, 400, and 500 as successful (indicating endpoint is accessible)

---

### 4. `test_integration_setup.py`
**Purpose**: Verifies the integration test setup is working correctly

**Test Cases**:
- `test_http_requests_working` - Validates HTTP request capability
- `test_api_base_url_configured` - Checks API base URL configuration
- `test_api_timeout_configured` - Validates API timeout settings
- `test_test_headers_configured` - Verifies test headers configuration
- `test_sample_data_fixtures` - Validates sample data fixtures
- `test_mock_requests_fixture` - Validates mock requests fixture
- `test_api_client_fixture` - Validates API client fixture
- `test_environment_variables` - Validates environment variables
- `test_pytest_configuration` - Validates pytest configuration files
- `test_integration_test_structure` - Validates test file structure
- `test_conftest_fixtures` - Validates conftest fixtures
- `test_buildspec_configuration` - Validates buildspec configuration
- `test_requirements_dependencies` - Validates required dependencies

**Total Tests**: 13

---

## API Endpoints Tested

### Health Check Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root health check endpoint |

### Optimization Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/optimise_metallizer` | POST | Metallizer optimization |
| `/api/optimise_setting` | POST | Setting optimization |
| `/api/optimise_wastage` | POST | Wastage optimization |
| `/api/optimise_hybrid` | POST | Hybrid optimization |
| `/api/optimise_knives` | POST | Knives optimization |

### Data Fetching Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/fetch_plan_data` | GET | Fetch plan data |
| `/api/comparison` | GET | Comparison data |
| `/api/product_results` | GET | Product results |
| `/api/get_details` | GET | Get user/details |
| `/api/update_results` | POST | Update results |

### Scheduler Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/changover_scheduler` | POST | Changeover scheduling |
| `/api/hybrid_scheduler` | POST | Hybrid scheduling |
| `/api/otif_scheduler` | POST | OTIF scheduling |
| `/api/slitting_orders` | GET | Get slitting orders |

### Planner Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/changeover_planner` | POST | Changeover planning |
| `/api/otif_planner` | POST | OTIF planning |
| `/api/hybrid_planner` | POST | Hybrid planning |
| `/api/sales_forecast` | GET | Get sales forecast |

### Campaign Management Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/fetch_campaign_plan` | GET | Fetch campaign plan |
| `/api/save_campaign_plan` | POST | Save campaign plan |
| `/api/update_campaign_plan` | PUT | Update campaign plan |
| `/api/delete_campaign_plan` | DELETE | Delete campaign plan |

### User and Machine Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/add_machine` | POST | Add machine configuration |
| `/get_machine_details` | GET | Get machine details |
| `/update_machine` | PUT | Update machine configuration |
| `/delete_machine` | DELETE | Delete machine |

### File Processing Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/upload_file` | POST | Upload file for processing |
| `/api/process_file` | POST | Process uploaded file |
| `/api/get_profile_picture` | GET | Get user profile picture |

### Additional Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/sap_integration` | POST | SAP system integration |
| `/api/get_secondary_data` | GET | Get secondary data |
| `/api/get_plant_list` | GET | Get plant list |

**Total Endpoints Tested**: 30+

---

## Test Configuration

### Configuration Files

#### `conftest.py`
- Defines pytest fixtures for API testing
- Configures API base URL and timeout
- Sets up test headers and authentication
- Provides sample data fixtures
- Manages API client instances

#### `config.py`
- API base URL configuration
- Timeout settings
- Testing mode flags
- Debug and logging configuration

#### `pytest.ini`
- Pytest discovery patterns
- Test output formatting
- Logging configuration
- Markers and markers configuration

#### `buildspec.yml`
- AWS CodeBuild configuration
- Python runtime version (3.11)
- Dependency installation
- Test execution commands
- Artifact collection

---

## Running Tests

### Prerequisites
- Python 3.11+
- pip package manager
- Access to the Module-DeckleOptimiser API

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nexus-Optima/Module-DeckleOptimiser-IntegrationTests.git
   cd Module-DeckleOptimiser-IntegrationTests
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables** (optional):
   ```bash
   export API_BASE_URL="https://trim-manager.appliedbellcurve.com"
   export API_TIMEOUT="30"
   export TESTING="true"
   ```

   Or use the setup script:
   ```bash
   source setup_env.sh
   ```

### Running All Tests

```bash
pytest -v
```

### Running Specific Test Files

```bash
# Health check tests only
pytest test_health_check.py -v

# API status report
pytest test_api_status_report.py -v

# API success validation
pytest test_api_success_validation.py -v

# Integration setup verification
pytest test_integration_setup.py -v
```

### Running Specific Test Cases

```bash
# Run specific test method
pytest test_health_check.py::TestHealthCheckEndpoint::test_health_check_success -v

# Run all tests in a class
pytest test_api_status_report.py::TestAPIStatusReport -v
```

### Running with JUnit XML Output

```bash
pytest --junitxml=test-results.xml -v
```

### Running with Coverage

```bash
pytest --cov=. --cov-report=html -v
```

---

## Test Results

### Test Output Format

Tests provide detailed output including:
- Endpoint URL being tested
- HTTP method used
- Response status code
- Response time
- Error messages (if any)
- Success/failure indicators

### JUnit XML Reports

Test results are generated in JUnit XML format for CI/CD integration:
- File: `test-results.xml`
- Contains test execution details
- Includes pass/fail status
- Captures test duration and errors

### Success Criteria

**Status Codes Considered Successful**:
- `200 OK` - Endpoint is working correctly
- `400 Bad Request` - Endpoint is accessible but requires valid parameters
- `500 Internal Server Error` - Endpoint is accessible but has server-side issues

**Failure Criteria**:
- `404 Not Found` - Endpoint does not exist
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Access denied
- Connection timeouts
- Network errors

### Test Statistics

- **Total Test Files**: 4
- **Total Test Cases**: ~43
- **Test Categories**: 9 endpoint categories
- **Endpoints Tested**: 30+

---

## CI/CD Integration

### AWS CodeBuild Integration

The test suite is integrated with AWS CodeBuild for automated testing in CI/CD pipelines.

#### Buildspec Configuration

The `buildspec.yml` file configures:
- Python 3.11 runtime
- Dependency installation
- Test execution
- Artifact collection

#### CodePipeline Integration

**Pipeline Flow**:
1. **Source Stage** - Fetch source code
2. **Test Stage** - Run integration tests
3. **Approval Stage** - Manual approval
4. **Deploy Stage** - Deploy to production

**Test Stage Configuration**:
- CodeBuild project: `Module-DeckleOptimiser-IntegrationTests`
- Buildspec file: `buildspec.yml`
- Environment variables configured
- Test results stored as artifacts

### Environment Variables in CI/CD

Required environment variables in CodeBuild:
- `API_BASE_URL` - Base URL for API (default: `https://trim-manager.appliedbellcurve.com`)
- `API_TIMEOUT` - Request timeout in seconds (default: `30`)
- `TESTING` - Testing mode flag (default: `true`)
- `DEBUG` - Debug mode (default: `false`)
- `LOG_LEVEL` - Logging level (default: `INFO`)

---

## Environment Variables

### Required Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `API_BASE_URL` | `https://trim-manager.appliedbellcurve.com` | Base URL for the API |
| `API_TIMEOUT` | `30` | Request timeout in seconds |

### Optional Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `TESTING` | `true` | Enable testing mode |
| `DEBUG` | `false` | Enable debug mode |
| `LOG_LEVEL` | `INFO` | Logging level |
| `API_TOKEN` | `""` | API authentication token |
| `API_KEY` | `""` | API authentication key |

### Setting Environment Variables

**Linux/Mac**:
```bash
export API_BASE_URL="https://trim-manager.appliedbellcurve.com"
export API_TIMEOUT="30"
```

**Windows**:
```cmd
set API_BASE_URL=https://trim-manager.appliedbellcurve.com
set API_TIMEOUT=30
```

**Using setup script**:
```bash
source setup_env.sh
```

---

## Troubleshooting

### Common Issues

#### 1. Connection Timeout
**Error**: `Connection timeout` or `Request timeout`

**Solutions**:
- Check API_BASE_URL is correct
- Verify network connectivity
- Increase API_TIMEOUT value
- Check firewall settings

#### 2. 404 Not Found
**Error**: `404 Not Found` for endpoints

**Solutions**:
- Verify endpoint URLs are correct
- Check API deployment status
- Ensure API is accessible

#### 3. Import Errors
**Error**: `ModuleNotFoundError` or `ImportError`

**Solutions**:
- Install dependencies: `pip install -r requirements.txt`
- Activate virtual environment
- Check Python version (3.11+)

#### 4. Test Failures
**Error**: Tests failing with unexpected status codes

**Solutions**:
- Check API is running and accessible
- Verify test data is valid
- Review API documentation for expected responses
- Check environment variables

#### 5. Buildspec Issues
**Error**: CodeBuild failures

**Solutions**:
- Verify buildspec.yml syntax
- Check environment variables in CodeBuild
- Ensure repository is accessible
- Verify Python version matches (3.11)

### Debug Mode

Enable debug mode for detailed output:
```bash
export DEBUG=true
export LOG_LEVEL=DEBUG
pytest -v -s
```

### Verbose Output

Run tests with verbose output:
```bash
pytest -vv
```

### Test Logs

Check test logs for detailed information:
```bash
pytest --log-cli-level=DEBUG -v
```

---

## Test Maintenance

### Adding New Tests

1. Create test file: `test_<feature>.py`
2. Import required fixtures from `conftest.py`
3. Create test class with descriptive name
4. Add test methods with descriptive names
5. Use appropriate assertions
6. Update this documentation

### Updating Endpoints

When API endpoints change:
1. Update endpoint URLs in test files
2. Update test data if needed
3. Verify test assertions
4. Update this documentation

### Test Data Management

- Sample data fixtures are in `conftest.py`
- Update fixtures when API contracts change
- Ensure test data is realistic but safe for testing

---

## Contact and Support

For issues or questions:
- Repository: https://github.com/Nexus-Optima/Module-DeckleOptimiser-IntegrationTests
- API Documentation: Refer to Module-DeckleOptimiser API documentation

---

## Version History

- **v1.0.0** (Current)
  - Initial test suite implementation
  - Health check endpoint tests
  - Comprehensive API status reporting
  - CI/CD integration with CodeBuild
  - Support for 30+ API endpoints

---

**Last Updated**: November 2024
**Test Suite Version**: 1.0.0
**Python Version**: 3.11+
**Pytest Version**: 8.4.2+

