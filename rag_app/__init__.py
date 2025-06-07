import os
import yaml
import logging
import logging.config

from .config import load_config

def setup_logging(default_path='configs/logging.yaml', default_level=logging.INFO):
    """Setup logging configuration."""
    if os.path.exists(default_path):
        with open(default_path, 'rt') as f:
            config = yaml.safe_load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        print(f'Warning: Logging configuration file {default_path} not found. Using default logging configuration.')

def create_app(config_path=None):
    '''
    App factory to initialize core components.
    Args:
        config_path (str): Path to the configuration file.
    Returns:
        dict: A dictionary containing the initialized components.
    '''
    setup_logging()
    logger = logging.getLogger('rag_app')

    config = load_config(config_path or 'configs/default_config.yaml')
    logger.info(f'Configuration loaded from {config_path or "default_config.yaml"}')

    return {
        'config': config,
        'logger': logger,
        # 'db': None,  # Placeholder for database connection
        # 'cache': None,  # Placeholder for cache system
        # 'search_engine': None,  # Placeholder for search engine
        # 'vector_store': None,  # Placeholder for vector store
        # 'llm': None,  # Placeholder for LLM client
        # 'retriever': None,  # Placeholder for retriever
        # 'generator': None,  # Placeholder for generator
        # 'pipeline': None,  # Placeholder for processing pipeline
    } # End of create_app function

