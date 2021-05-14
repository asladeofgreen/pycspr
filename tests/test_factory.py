import random

from pycspr.domain.types import CLType, NamedArg



def test_api(LIB):
    assert LIB.create_cl_value is not None
    assert LIB.create_named_arg is not None
    assert LIB.create_session_args_for_a_transfer is not None


def test_create_cl_value(LIB):
    assert isinstance(
        LIB.create_cl_value("a-string-cl-value", LIB.types.CLType.STRING),
        LIB.types.CLValue
        )


def test_create_named_arg(LIB):
    arg = LIB.create_named_arg("a-string-arg", LIB.types.CLType.STRING, "Al-Kindi")
    assert isinstance(arg, LIB.types.NamedArg)


def test_create_session_args_for_a_transfer(LIB):
    args = LIB.create_session_args_for_a_transfer(
        1e9,
        bytes([]),
        random.randint(0, 124),
        "A-PURSE-UREF",
        )
    assert isinstance(args, list)
    for arg in args:
        assert isinstance(arg, NamedArg)
