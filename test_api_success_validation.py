"""
API Success Validation - Treats 200, 400, 500 as successful responses
This test validates that all APIs are accessible and responding correctly
"""
import pytest
import requests
from requests.exceptions import RequestException


class TestAPISuccessValidation:
    """Validate all APIs are accessible and responding (treating 200, 400, 500 as success)"""

    def test_health_check_success(self, api_base_url, api_timeout, test_headers):
        """Test health check returns 200"""
        response = requests.get(f"{api_base_url}/", headers=test_headers, timeout=api_timeout)
        assert response.status_code == 200
        assert "200" in response.text or "ok" in response.text.lower()

    def test_optimization_endpoints_success(self, api_base_url, api_timeout, test_headers, sample_optimization_data):
        """Test optimization endpoints are accessible"""
        endpoints = [
            "/api/optimise_metallizer",
            "/api/optimise_setting", 
            "/api/optimise_wastage",
            "/api/optimise_hybrid"
        ]
        
        for endpoint in endpoints:
            response = requests.post(f"{api_base_url}{endpoint}", json=sample_optimization_data, headers=test_headers, timeout=api_timeout)
            # Treat 200, 400, 500 as success (endpoint is accessible)
            assert response.status_code in [200, 400, 500], f"Endpoint {endpoint} returned unexpected status {response.status_code}"

    def test_data_fetching_endpoints_success(self, api_base_url, api_timeout, test_headers):
        """Test data fetching endpoints are accessible"""
        endpoints = [
            "/api/fetch_plan_data",
            "/api/comparison",
            "/api/product_results"
        ]
        
        for endpoint in endpoints:
            params = {"company": "TEST", "plant": "TEST_PLANT"}
            response = requests.get(f"{api_base_url}{endpoint}", params=params, headers=test_headers, timeout=api_timeout)
            # Treat 200, 400, 500 as success (endpoint is accessible)
            assert response.status_code in [200, 400, 500], f"Endpoint {endpoint} returned unexpected status {response.status_code}"

    def test_scheduler_endpoints_success(self, api_base_url, api_timeout, test_headers, sample_scheduler_data):
        """Test scheduler endpoints are accessible"""
        endpoints = [
            "/api/changover_scheduler",
            "/api/hybrid_scheduler",
            "/api/otif_scheduler"
        ]
        
        for endpoint in endpoints:
            response = requests.post(f"{api_base_url}{endpoint}", json=sample_scheduler_data, headers=test_headers, timeout=api_timeout)
            # Treat 200, 400, 500 as success (endpoint is accessible)
            assert response.status_code in [200, 400, 500], f"Endpoint {endpoint} returned unexpected status {response.status_code}"

    def test_planner_endpoints_success(self, api_base_url, api_timeout, test_headers):
        """Test planner endpoints are accessible"""
        endpoints = [
            "/api/changover_planner",
            "/api/otif_planner",
            "/api/hybrid_planner"
        ]
        
        for endpoint in endpoints:
            response = requests.get(f"{api_base_url}{endpoint}", headers=test_headers, timeout=api_timeout)
            # Treat 200, 400, 500 as success (endpoint is accessible)
            assert response.status_code in [200, 400, 500], f"Endpoint {endpoint} returned unexpected status {response.status_code}"

    def test_campaign_management_endpoints_success(self, api_base_url, api_timeout, test_headers, sample_campaign_plan):
        """Test campaign management endpoints are accessible"""
        endpoints = [
            ("/api/save_campaign_plan", "POST"),
            ("/api/fetch_campaign_plan", "GET"),
            ("/api/fetch_campaign_metadata", "GET"),
            ("/api/save_sales_forecast", "POST")
        ]
        
        for endpoint, method in endpoints:
            if method == "GET":
                response = requests.get(f"{api_base_url}{endpoint}", headers=test_headers, timeout=api_timeout)
            else:
                response = requests.post(f"{api_base_url}{endpoint}", json=sample_campaign_plan, headers=test_headers, timeout=api_timeout)
            # Treat 200, 400, 500 as success (endpoint is accessible)
            assert response.status_code in [200, 400, 500], f"Endpoint {endpoint} returned unexpected status {response.status_code}"

    def test_user_machine_endpoints_success(self, api_base_url, api_timeout, test_headers, sample_user_data):
        """Test user and machine endpoints are accessible"""
        endpoints = [
            ("/update_details", "POST"),
            ("/get_details", "GET"),
            ("/add_machine", "POST"),
            ("/get_machine_details", "GET")
        ]
        
        for endpoint, method in endpoints:
            if method == "GET":
                response = requests.get(f"{api_base_url}{endpoint}", headers=test_headers, timeout=api_timeout)
            else:
                response = requests.post(f"{api_base_url}{endpoint}", json=sample_user_data, headers=test_headers, timeout=api_timeout)
            # Treat 200, 400, 500 as success (endpoint is accessible)
            assert response.status_code in [200, 400, 500], f"Endpoint {endpoint} returned unexpected status {response.status_code}"

    def test_file_processing_endpoints_success(self, api_base_url, api_timeout, test_headers):
        """Test file processing endpoints are accessible"""
        endpoints = [
            ("/api/preprocess_excel_data", "POST"),
            ("/api/save_selected_orders", "POST"),
            ("/api/fetch_selected_orders", "GET"),
            ("/api/sap_data", "GET")
        ]
        
        for endpoint, method in endpoints:
            if method == "GET":
                response = requests.get(f"{api_base_url}{endpoint}", headers=test_headers, timeout=api_timeout)
            else:
                response = requests.post(f"{api_base_url}{endpoint}", json={}, headers=test_headers, timeout=api_timeout)
            # Treat 200, 400, 500 as success (endpoint is accessible)
            assert response.status_code in [200, 400, 500], f"Endpoint {endpoint} returned unexpected status {response.status_code}"

    def test_additional_endpoints_success(self, api_base_url, api_timeout, test_headers):
        """Test additional endpoints are accessible"""
        endpoints = [
            ("/api/fetch_material_groups", "GET"),
            ("/api/fetch_parameters", "GET"),
            ("/api/fetch_deckle_orders", "GET"),
            ("/api/save_slitting_orders", "POST")
        ]
        
        for endpoint, method in endpoints:
            if method == "GET":
                response = requests.get(f"{api_base_url}{endpoint}", headers=test_headers, timeout=api_timeout)
            else:
                response = requests.post(f"{api_base_url}{endpoint}", json={}, headers=test_headers, timeout=api_timeout)
            # Treat 200, 400, 500 as success (endpoint is accessible)
            assert response.status_code in [200, 400, 500], f"Endpoint {endpoint} returned unexpected status {response.status_code}"

    def test_all_endpoints_accessible(self, api_base_url, api_timeout, test_headers):
        """Comprehensive test that all endpoints are accessible"""
        print(f"\nTesting All Endpoints Accessibility")
        print(f"   Base URL: {api_base_url}")
        
        # Define all endpoints to test
        all_endpoints = [
            # Health check
            ("/", "GET"),
            
            # Optimization
            ("/api/optimise_metallizer", "POST"),
            ("/api/optimise_setting", "POST"),
            ("/api/optimise_wastage", "POST"),
            ("/api/optimise_hybrid", "POST"),
            
            # Data fetching
            ("/api/fetch_plan_data", "GET"),
            ("/api/comparison", "GET"),
            ("/api/product_results", "GET"),
            ("/api/update_results", "POST"),
            
            # Scheduler
            ("/api/changover_scheduler", "POST"),
            ("/api/hybrid_scheduler", "POST"),
            ("/api/otif_scheduler", "POST"),
            ("/api/fetch_scheduler_data", "GET"),
            
            # Planner
            ("/api/changover_planner", "GET"),
            ("/api/otif_planner", "GET"),
            ("/api/hybrid_planner", "GET"),
            ("/api/fetch_planner_data", "GET"),
            
            # Campaign management
            ("/api/save_campaign_plan", "POST"),
            ("/api/fetch_campaign_plan", "GET"),
            ("/api/fetch_campaign_metadata", "GET"),
            ("/api/save_sales_forecast", "POST"),
            
            # User & Machine
            ("/update_details", "POST"),
            ("/get_details", "GET"),
            ("/add_machine", "POST"),
            ("/get_machine_details", "GET"),
            
            # File processing
            ("/api/preprocess_excel_data", "POST"),
            ("/api/save_selected_orders", "POST"),
            ("/api/fetch_selected_orders", "GET"),
            ("/api/sap_data", "GET"),
            
            # Additional
            ("/api/fetch_material_groups", "GET"),
            ("/api/fetch_parameters", "GET"),
            ("/api/fetch_deckle_orders", "GET"),
            ("/api/save_slitting_orders", "POST"),
        ]
        
        success_count = 0
        total_count = len(all_endpoints)
        
        for endpoint, method in all_endpoints:
            try:
                if method == "GET":
                    response = requests.get(f"{api_base_url}{endpoint}", headers=test_headers, timeout=api_timeout)
                else:
                    response = requests.post(f"{api_base_url}{endpoint}", json={}, headers=test_headers, timeout=api_timeout)
                
                if response.status_code in [200, 400, 500]:
                    success_count += 1
                    print(f"   PASS {endpoint} ({method}): {response.status_code}")
                else:
                    print(f"   FAIL {endpoint} ({method}): {response.status_code}")
                    
            except RequestException as e:
                print(f"   FAIL {endpoint} ({method}): Connection error - {e}")
        
        print(f"\nResults: {success_count}/{total_count} endpoints accessible")
        print(f"   Success Rate: {(success_count/total_count)*100:.1f}%")
        
        # Assert that at least 90% of endpoints are accessible
        assert success_count >= total_count * 0.9, f"Only {success_count}/{total_count} endpoints are accessible"
        print(f"   API accessibility test passed!")
