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
    # {
    #   "account_hash": "account-hash-559d0575e0c1af1c1f16c7b391e732453fd83ad009b728f79b47f2b5a6eb3d05",
    #   "action_thresholds": {
    #     "deployment": 1,
    #     "key_management": 1
    #   },
    #   "associated_keys": [
    #     {
    #       "account_hash": "account-hash-559d0575e0c1af1c1f16c7b391e732453fd83ad009b728f79b47f2b5a6eb3d05",
    #       "weight": 1
    #     }
    #   ],
    #   "main_purse": "uref-827d5984270fed5aaaf076e1801733414a307ed8c5d85cad8ebe6265ba887b3a-007",
    #   "named_keys": []
    # }

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


def test_04_get_account_balance(LIB, account_main_purse_uref, state_root_hash):
    # Example API response.
    # 1000000000000000000000000000000000

    # Assert API response.
    def _assert(response):
        assert isinstance(response, int)
        assert response >= 0

    # Invoke API.
    _assert(LIB.get_account_balance(account_main_purse_uref, state_root_hash))


def test_05_get_auction_info(LIB):
    # Example API response.
    # {
    # "api_version": "1.0.0",
    # "chainspec_name": "casper-net-1",
    # "starting_state_root_hash": "0762..4ef7",
    # "peers": [
    #     {
    #     "node_id": "NodeId::Tls(2933..32bd)",
    #     "address": "127.0.0.1:34554"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(3922..e3e8)",
    #     "address": "127.0.0.1:34557"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(618a..4460)",
    #     "address": "127.0.0.1:34556"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(bc9f..1270)",
    #     "address": "127.0.0.1:34555"
    #     }
    # ],
    # "last_added_block_info": {
    #     "hash": "9391ed4dc9075a3cad4c506bbc8b9185232f250da98165801aa47a7d97540591",
    #     "timestamp": "2021-04-13T14:07:25.696Z",
    #     "era_id": 218,
    #     "height": 2395,
    #     "state_root_hash": "601d694f2e5815430268fa5269f9325abd380620f2fd1abdc430bc8dd0503985",
    #     "creator": "01b41fe74903a0e37044bdeded8876387ac7e7b608b5b6ef7382e936991d1151a7"
    # },
    # "our_public_signing_key": "013156788978cf17ee36b6bf032752161c223cd16ed9d5e076e28e7eae0408525c",
    # "round_length": "4s 96ms",
    # "next_upgrade": null,
    # "build_version": "1.0.0-4dc1d48a"
    # }

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)

    # Invoke API.
    _assert(LIB.get_auction_info())


def test_06_get_node_peers(LIB):
    # Example API response.
    # [
    # {
    #     "node_id": "NodeId::Tls(2933..32bd)",
    #     "address": "127.0.0.1:34554"
    # },
    # {
    #     "node_id": "NodeId::Tls(3922..e3e8)",
    #     "address": "127.0.0.1:34557"
    # },
    # {
    #     "node_id": "NodeId::Tls(618a..4460)",
    #     "address": "127.0.0.1:34556"
    # },
    # {
    #     "node_id": "NodeId::Tls(bc9f..1270)",
    #     "address": "127.0.0.1:34555"
    # }
    # ]

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)

    # Invoke API.
    _assert(LIB.get_node_peers())


def test_07_get_node_status(LIB):
    # Example API response.
    # {
    # "api_version": "1.0.0",
    # "chainspec_name": "casper-net-1",
    # "starting_state_root_hash": "0762..4ef7",
    # "peers": [
    #     {
    #     "node_id": "NodeId::Tls(2933..32bd)",
    #     "address": "127.0.0.1:34554"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(3922..e3e8)",
    #     "address": "127.0.0.1:34557"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(618a..4460)",
    #     "address": "127.0.0.1:34556"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(bc9f..1270)",
    #     "address": "127.0.0.1:34555"
    #     }
    # ],
    # "last_added_block_info": {
    #     "hash": "9391ed4dc9075a3cad4c506bbc8b9185232f250da98165801aa47a7d97540591",
    #     "timestamp": "2021-04-13T14:07:25.696Z",
    #     "era_id": 218,
    #     "height": 2395,
    #     "state_root_hash": "601d694f2e5815430268fa5269f9325abd380620f2fd1abdc430bc8dd0503985",
    #     "creator": "01b41fe74903a0e37044bdeded8876387ac7e7b608b5b6ef7382e936991d1151a7"
    # },
    # "our_public_signing_key": "013156788978cf17ee36b6bf032752161c223cd16ed9d5e076e28e7eae0408525c",
    # "round_length": "4s 96ms",
    # "next_upgrade": null,
    # "build_version": "1.0.0-4dc1d48a"
    # }

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)

    # Invoke API.
    _assert(LIB.get_node_status())


def test_08_get_block(LIB):
    # Example API response.
    # {
    # "api_version": "1.0.0",
    # "chainspec_name": "casper-net-1",
    # "starting_state_root_hash": "0762..4ef7",
    # "peers": [
    #     {
    #     "node_id": "NodeId::Tls(2933..32bd)",
    #     "address": "127.0.0.1:34554"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(3922..e3e8)",
    #     "address": "127.0.0.1:34557"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(618a..4460)",
    #     "address": "127.0.0.1:34556"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(bc9f..1270)",
    #     "address": "127.0.0.1:34555"
    #     }
    # ],
    # "last_added_block_info": {
    #     "hash": "9391ed4dc9075a3cad4c506bbc8b9185232f250da98165801aa47a7d97540591",
    #     "timestamp": "2021-04-13T14:07:25.696Z",
    #     "era_id": 218,
    #     "height": 2395,
    #     "state_root_hash": "601d694f2e5815430268fa5269f9325abd380620f2fd1abdc430bc8dd0503985",
    #     "creator": "01b41fe74903a0e37044bdeded8876387ac7e7b608b5b6ef7382e936991d1151a7"
    # },
    # "our_public_signing_key": "013156788978cf17ee36b6bf032752161c223cd16ed9d5e076e28e7eae0408525c",
    # "round_length": "4s 96ms",
    # "next_upgrade": null,
    # "build_version": "1.0.0-4dc1d48a"
    # }

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


def test_09_get_block_by_hash(LIB, block_hash):
    # Example API response.
    # {
    # "api_version": "1.0.0",
    # "chainspec_name": "casper-net-1",
    # "starting_state_root_hash": "0762..4ef7",
    # "peers": [
    #     {
    #     "node_id": "NodeId::Tls(2933..32bd)",
    #     "address": "127.0.0.1:34554"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(3922..e3e8)",
    #     "address": "127.0.0.1:34557"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(618a..4460)",
    #     "address": "127.0.0.1:34556"
    #     },
    #     {
    #     "node_id": "NodeId::Tls(bc9f..1270)",
    #     "address": "127.0.0.1:34555"
    #     }
    # ],
    # "last_added_block_info": {
    #     "hash": "9391ed4dc9075a3cad4c506bbc8b9185232f250da98165801aa47a7d97540591",
    #     "timestamp": "2021-04-13T14:07:25.696Z",
    #     "era_id": 218,
    #     "height": 2395,
    #     "state_root_hash": "601d694f2e5815430268fa5269f9325abd380620f2fd1abdc430bc8dd0503985",
    #     "creator": "01b41fe74903a0e37044bdeded8876387ac7e7b608b5b6ef7382e936991d1151a7"
    # },
    # "our_public_signing_key": "013156788978cf17ee36b6bf032752161c223cd16ed9d5e076e28e7eae0408525c",
    # "round_length": "4s 96ms",
    # "next_upgrade": null,
    # "build_version": "1.0.0-4dc1d48a"
    # }

    # Assert API response.
    def _assert(response):
        assert isinstance(response, dict)
        assert "body" in response        
        assert "hash" in response        
        assert "header" in response        
        assert "proofs" in response        

    # Invoke API.
    _assert(LIB.get_block(block_hash))
