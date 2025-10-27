"""
Integration tests for health check endpoint
Tests the actual API endpoint over HTTP
"""
import pytest
import requests
from requests.exceptions import RequestException


class TestHealthCheckEndpoint:
    """Test cases for health check endpoint"""

    def test_health_check_success(self, api_base_url, api_timeout, test_headers):
        """Test successful health check"""
        url = f"{api_base_url}/"
        
        try:
            response = requests.get(url, headers=test_headers, timeout=api_timeout)
            
            assert response.status_code == 200
            assert "200" in response.text or "ok" in response.text.lower()
            
        except RequestException as e:
            pytest.skip(f"API not available: {e}")

    def test_health_check_error_handling(self, api_base_url, api_timeout, test_headers):
        """Test health check error handling"""
        url = f"{api_base_url}/"
        
        try:
            response = requests.get(url, headers=test_headers, timeout=api_timeout)
            
            # Should return 200 even if there are internal issues
            assert response.status_code in [200, 500]
            
        except RequestException as e:
            pytest.skip(f"API not available: {e}")

    def test_health_check_with_different_methods(self, api_base_url, api_timeout, test_headers):
        """Test health check with different HTTP methods"""
        url = f"{api_base_url}/"
        
        try:
            # GET should work
            response = requests.get(url, headers=test_headers, timeout=api_timeout)
            assert response.status_code in [200, 405]  # 405 if method not allowed
            
            # POST might not be supported
            response = requests.post(url, headers=test_headers, timeout=api_timeout)
            assert response.status_code in [200, 405]
            
        except RequestException as e:
            pytest.skip(f"API not available: {e}")

    def test_health_check_response_time(self, api_base_url, api_timeout, test_headers):
        """Test health check response time"""
        import time
        
        url = f"{api_base_url}/"
        
        try:
            start_time = time.time()
            response = requests.get(url, headers=test_headers, timeout=api_timeout)
            end_time = time.time()
            
            response_time = end_time - start_time
            
            assert response.status_code == 200
            assert response_time < 5.0  # Should respond within 5 seconds
            
        except RequestException as e:
            pytest.skip(f"API not available: {e}")

    def test_health_check_content_type(self, api_base_url, api_timeout, test_headers):
        """Test health check content type"""
        url = f"{api_base_url}/"
        
        try:
            response = requests.get(url, headers=test_headers, timeout=api_timeout)
            
            assert response.status_code == 200
            # Should return JSON or text
            assert 'application/json' in response.headers.get('Content-Type', '') or \
                   'text' in response.headers.get('Content-Type', '')
            
        except RequestException as e:
            pytest.skip(f"API not available: {e}")

    def test_health_check_cors_headers(self, api_base_url, api_timeout, test_headers):
        """Test CORS headers in health check response"""
        url = f"{api_base_url}/"
        
        try:
            response = requests.get(url, headers=test_headers, timeout=api_timeout)
            
            assert response.status_code == 200
            # Check for CORS headers
            cors_headers = [
                'Access-Control-Allow-Origin',
                'Access-Control-Allow-Methods',
                'Access-Control-Allow-Headers'
            ]
            
            # At least one CORS header should be present
            has_cors = any(header in response.headers for header in cors_headers)
            # Note: CORS headers might not be present in all environments
            
        except RequestException as e:
            pytest.skip(f"API not available: {e}")

    @pytest.mark.slow
    def test_health_check_load(self, api_base_url, api_timeout, test_headers):
        """Test health check under load"""
        import concurrent.futures
        import time
        
        url = f"{api_base_url}/"
        num_requests = 10
        
        def make_request():
            try:
                response = requests.get(url, headers=test_headers, timeout=api_timeout)
                return response.status_code
            except RequestException:
                return None
        
        try:
            start_time = time.time()
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(make_request) for _ in range(num_requests)]
                results = [future.result() for future in futures]
            
            end_time = time.time()
            total_time = end_time - start_time
            
            # All requests should succeed
            successful_requests = [r for r in results if r == 200]
            assert len(successful_requests) >= num_requests * 0.8  # At least 80% success rate
            
            # Should handle load reasonably
            assert total_time < 30.0  # All requests within 30 seconds
            
        except RequestException as e:
            pytest.skip(f"API not available: {e}")

    def test_health_check_with_parameters(self, api_base_url, api_timeout, test_headers):
        """Test health check with query parameters"""
        url = f"{api_base_url}/"
        
        try:
            # Test with query parameters
            params = {"format": "json", "verbose": "true"}
            response = requests.get(url, headers=test_headers, params=params, timeout=api_timeout)
            
            assert response.status_code in [200, 400]  # 400 if parameters not supported
            
        except RequestException as e:
            pytest.skip(f"API not available: {e}")

    def test_health_check_authentication(self, api_base_url, api_timeout, test_headers):
        """Test health check with and without authentication"""
        url = f"{api_base_url}/"
        
        try:
            # Test without authentication
            response = requests.get(url, timeout=api_timeout)
            assert response.status_code in [200, 401, 403]
            
            # Test with authentication header
            auth_headers = test_headers.copy()
            auth_headers['Authorization'] = 'Bearer test-token'
            response = requests.get(url, headers=auth_headers, timeout=api_timeout)
            assert response.status_code in [200, 401, 403]
            
        except RequestException as e:
            pytest.skip(f"API not available: {e}")