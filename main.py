from rag_app import create_app
from rag_app.utils.logger_utils import log_action, log_exception

def main():
    """
    Main function to initialize the application and perform basic operations.
    """
    try:
        app = create_app('configs/default_config.yaml')
        log_action('main', 'Application initialized', {'config': app['config']}, 'info')
    except Exception as e:
        log_exception('main', 'Error during application initialization or operation', e)


if __name__ == '__main__':
    main()