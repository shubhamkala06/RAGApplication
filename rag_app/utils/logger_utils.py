import logging
import traceback
import json

logger = logging.getLogger('rag_app')

def log_action(module_name:str, action:str, extra_info:dict=None, level:str='info'):
    """
    Log an action with module name, action type, and optional extra information.
    
    Args:
        module_name (str): Name of the module performing the action.
        action (str): Description of the action being logged.
        extra_info (dict, optional): Additional information to log. Defaults to None.
        level (str): Logging level ('debug', 'info', 'warning', 'error', 'critical'). Defaults to 'info'.
    """
    log_message = {
        'module': module_name,
        'action': action,
        'extra_info': extra_info or {}
    }
    
    log_func = getattr(logger, level, logger.info)
    log_func(json.dumps(log_message, ensure_ascii=False, indent=2))

def log_exception(module_name:str, action:str, exception:Exception):
    """
    Log an exception with module name, action type, and exception details.
    
    Args:
        module_name (str): Name of the module where the exception occurred.
        action (str): Description of the action being performed when the exception occurred.
        exception (Exception): The exception instance to log.
    """
    log_message = {
        'module': module_name,
        'action': action,
        'exception': str(exception),
        'traceback': traceback.format_exc()
    }
    
    logger.error(json.dumps(log_message, ensure_ascii=False, indent=2))