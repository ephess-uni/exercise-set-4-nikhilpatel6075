""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    with open(logfile, 'r') as shutdown_logfile:
        
        shutdown_logfile_content = shutdown_logfile.read()
    
    shutdown_logfile_content = shutdown_logfile_content.splitlines()
    
    get_shutdown_event_list = list()
    
    for cont in shutdown_logfile_content:
        
        if 'Shutdown initiated' in cont :
            
            get_shutdown_event_list.append(cont)
        
    return get_shutdown_event_list


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
