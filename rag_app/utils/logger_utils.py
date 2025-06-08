import logging


logger = logging.getLogger('rag_app')

def log_action(module_name:str, action:str, extra_info:dict=None, level:str='info') -> None:
    """
    Log an action with module name, action type, and optional extra information.
    
    Args:
        module_name (str): Name of the module performing the action.
        action (str): Description of the action being logged.
        extra_info (dict, optional): Additional information to log. Defaults to None.
        level (str): Logging level ('debug', 'info', 'warning', 'error', 'critical'). Defaults to 'info'.
    """
    if level.lower() not in ['debug', 'info', 'warning', 'error', 'critical']:
        raise ValueError(f"Invalid log level: {level}.")
    
    log_func = getattr(logger, level.lower(), logger.info)
    log_func(
        action,
        extra={
            'context': {
                # 'request_id': request_id,
                # 'conversation_id': conversation_id,
                # 'user_id': user_id,
                'module_name': module_name,
                'action': action,
                'extra_info': extra_info or {},
                'exception': None
            }
        }
    )

    

def log_exception(module_name:str, action:str, exception:Exception) -> None:
    """
    Log an exception with module name, action type, and exception details.
    
    Args:
        module_name (str): Name of the module where the exception occurred.
        action (str): Description of the action being performed when the exception occurred.
        exception (Exception): The exception instance to log.
    """
    logger.error(
        action,
        exc_info=True,
        extra={
            'context': {
                # 'request_id': request_id,
                # 'conversation_id': conversation_id,
                # 'user_id': user_id,
                'module_name': module_name,
                'action': action,
                'extra_info': {},
                'exception': {
                    'type': type(exception).__name__,
                    'message': str(exception)
                }
            }
        }
    )