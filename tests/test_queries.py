import pytest



def test_01_get_chain_state_root_hash(LIB):
    # Example API response.
    # 601d694f2e5815430268fa5269f9325abd380620f2fd1abdc430bc8dd0503985

    # Assert API response.
    def _assert(response):
        assert isinstance(response, str)
        assert len(response) == 64

    # Invoke API.
    for block_id in (None, 1):
        _assert(LIB.get_chain_state_root_hash(block_id))


def test_02_get_account_info(LIB, account_key, state_root_hash):
    # Example API response.
    # See api_reponses/state_get_item.account.json

    # Assert API response.
    # TODO: use jsonschema derived from RPC schema
    def _assert(response):
        assert isinstance(response, dict)
        assert "account_hash" in response
        assert "action_thresholds" in response
        assert "deployment" in response["action_thresholds"]
        assert "key_management" in response["action_thresholds"]
        assert "associated_keys" in response
        assert len(response["associated_keys"]) >= 1
        for key in response["associated_keys"]:
            assert "account_hash" in key
            assert "weight" in key
        assert "main_purse" in response
        assert "named_keys" in response
        assert isinstance(response["named_keys"], list)

    # Invoke API.
    _assert(LIB.get_account_info(account_key, state_root_hash))


def test_03_get_account_main_purse_uref(LIB, account_key, state_root_hash):
    # Example API response.
    # uref-827d5984270fed5aaaf076e1801733414a307ed8c5d85cad8ebe6265ba887b3a-007

    # Assert API response.
    def _assert(response):
        assert isinstance(response, str)
        parts = response.split("-")
        assert len(parts) == 3
        assert parts[0] == "uref"
        assert len(parts[1]) == 64
        assert len(parts[2]) == 3

    # Invoke API.
    _assert(LIB.get_account_main_purse_uref(account_key, state_root_hash))


def test_04_get_account_balance_01(LIB, account_main_purse_uref, state_root_hash):
    # Example API response.
    # 1000000000000000000000000000000000

    # Assert API response.
    def _assert(response):
        assert isinstance(response, int)
        assert response >= 0

    # Invoke API.
    _assert(LIB.get_account_balance(account_main_purse_uref, state_root_hash))


def test_04_get_account_balance_02(LIB, account_main_purse_uref, state_root_hash):
    # Example API response.
    # See api_reponses/state_get_balance.json

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)

    # Invoke API.
    _assert(LIB.get_account_balance(account_main_purse_uref, state_root_hash, parse_response=False))


def test_05_get_auction_info(LIB):
    # Example API response.
    # See api_reponses/state_get_auction_info.account.json

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)

    # Invoke API.
    _assert(LIB.get_auction_info())


def test_06_get_node_metrics(LIB):
    # Example API response.
    # See api_reponses/rest_metrics.json

    # Assert API response.
    def _assert(response):
        assert isinstance(response, list)

    # Invoke API.
    _assert(LIB.get_node_metrics())


def test_07_get_node_peers(LIB):
    # Example API response.
    # See api_reponses/info_get_peers.json

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)

    # Invoke API.
    _assert(LIB.get_node_peers())


def test_08_get_node_status(LIB):
    # Example API response.
    # See api_reponses/info_get_status.json

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)

    # Invoke API.
    _assert(LIB.get_node_status())


def test_09_get_block_01(LIB):
    # Example API response.
    # See api_reponses/chain_get_block.json

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)
        assert "body" in response        
        assert "hash" in response        
        assert "header" in response        
        assert "proofs" in response        

    # Invoke API.
    for block_id in (None, 1):
        _assert(LIB.get_block(block_id))


def test_09_get_block_02(LIB, block_hash):
    # Example API response.
    # See api_reponses/chain_get_block.json

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)
        assert "body" in response        
        assert "hash" in response        
        assert "header" in response        
        assert "proofs" in response        

    # Invoke API.
    _assert(LIB.get_block(block_hash))
