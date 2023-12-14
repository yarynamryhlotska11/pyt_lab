import logging

# Logging settings
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger instance for the current module
logger = logging.getLogger(__name__)
