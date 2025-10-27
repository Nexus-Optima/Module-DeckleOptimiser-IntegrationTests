#!/bin/bash

# Setup environment variables for Module-DeckleOptimiser Integration Tests
# This script sets up the environment variables for testing

echo "Setting up environment variables for Module-DeckleOptimiser Integration Tests..."

# Export environment variables
export API_BASE_URL="https://trim-manager.appliedbellcurve.com"
export API_TIMEOUT="30"
export TESTING="true"

echo "✅ Environment variables set:"
echo "  API_BASE_URL: $API_BASE_URL"
echo "  API_TIMEOUT: $API_TIMEOUT"
echo "  TESTING: $TESTING"

echo ""
echo "You can now run the tests with:"
echo "  pytest"
echo "  pytest test_health_check.py -v"
echo "  pytest test_api_endpoints_example.py -v"
