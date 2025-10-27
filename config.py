"""
Configuration file for Module-DeckleOptimiser Integration Tests
"""
import os

# API Configuration
API_BASE_URL = os.getenv('API_BASE_URL', 'https://trim-manager.appliedbellcurve.com')
API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))
TESTING = os.getenv('TESTING', 'true').lower() == 'true'

# Optional: Authentication (if required)
API_TOKEN = os.getenv('API_TOKEN', '')
API_KEY = os.getenv('API_KEY', '')

# Optional: Additional configuration
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Print configuration for verification
if __name__ == "__main__":
    print("Module-DeckleOptimiser Integration Tests Configuration:")
    print(f"API_BASE_URL: {API_BASE_URL}")
    print(f"API_TIMEOUT: {API_TIMEOUT}")
    print(f"TESTING: {TESTING}")
    print(f"DEBUG: {DEBUG}")
    print(f"LOG_LEVEL: {LOG_LEVEL}")
