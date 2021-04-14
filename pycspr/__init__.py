#  8b,dPPYba,   8b       d8   ,adPPYba,  ,adPPYba,  8b,dPPYba,   8b,dPPYba,  
#  88P'    "8a  `8b     d8'  a8"     ""  I8[    ""  88P'    "8a  88P'   "Y8  
#  88       d8   `8b   d8'   8b           `"Y8ba,   88       d8  88          
#  88b,   ,a8"    `8b,d8'    "8a,   ,aa  aa    ]8I  88b,   ,a8"  88          
#  88`YbbdP"'       Y88'      `"Ybbd8"'  `"YbbdP"'  88`YbbdP"'   88          
#  88               d8'                             88                       
#  88              d8'                              88                       

from pycspr import crypto
from pycspr.connection_info import ConnectionInfo
from pycspr.crypto  import get_account_hash
from pycspr.queries import get_account_balance
from pycspr.queries import get_account_info
from pycspr.queries import get_account_main_purse_uref
from pycspr.queries import get_auction_info
from pycspr.queries import get_block
from pycspr.queries import get_chain_state_root_hash
from pycspr.queries import get_era_info
from pycspr.queries import get_node_metrics
from pycspr.queries import get_node_peers
from pycspr.queries import get_node_status
from pycspr.queries import get_switch_block



# Lib metadata.
__title__ = "pycspr"
__version__ = "0.1.0"
__author__ = "osbitwhoei - object swarms bath in the white heat of event infernoes"
__license__ = "Apache 2.0"

# Node connection info.
CONNECTION = None


def initialise(connection_info: ConnectionInfo):
    """Library initialiser - to beinokved prior to usage.
    
    :param connection_info: Information requireed to connect to a node.
    
    """
    global CONNECTION

    if CONNECTION is None:
        CONNECTION = connection_info
