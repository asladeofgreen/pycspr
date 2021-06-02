from pycspr.types.cl import CLType
from pycspr.types.cl import CLTypeInfo
from pycspr.types.cl import CLTypeInfoForByteArray
from pycspr.types.cl import CLTypeInfoForList
from pycspr.types.cl import CLTypeInfoForMap
from pycspr.types.cl import CLTypeInfoForOption
from pycspr.types.cl import CLTypeInfoForTuple1
from pycspr.types.cl import CLTypeInfoForTuple2
from pycspr.types.cl import CLTypeInfoForTuple3


def create_type_info(typeof: CLType) -> CLTypeInfo:
    return CLTypeInfo(typeof)


def create_type_info_for_byte_array(size: int) -> CLTypeInfoForByteArray:
    return CLTypeInfoForByteArray(
        typeof=CLType.BYTE_ARRAY,
        size=size
    )


def create_type_info_for_list(inner_type_info: CLType) -> CLTypeInfoForList:
    return CLTypeInfoForList(
        typeof=CLType.LIST,
        inner_type_info=inner_type_info
    )


def create_type_info_for_map(key_type_info: CLTypeInfo, value_type_info: CLTypeInfo) -> CLTypeInfoForMap:
    return CLTypeInfoForMap(
        typeof=CLType.MAP,
        key_type_info=key_type_info,
        value_type_info=value_type_info
    )


def create_type_info_for_option(inner_type_info: CLTypeInfo):
    return CLTypeInfoForOption(
        typeof=CLType.OPTION,
        inner_type_info=inner_type_info
    )


def create_type_info_for_tuple_1(t0_type_info: CLTypeInfo):
    return CLTypeInfoForTuple1(
        typeof=CLType.TUPLE_1,
        t0_type_info=t0_type_info
    )


def create_type_info_for_tuple_2(t0_type_info: CLTypeInfo, t1_type_info: CLTypeInfo):
    return CLTypeInfoForTuple2(
        typeof=CLType.TUPLE_1,
        t0_type_info=t0_type_info,
        t1_type_info=t1_type_info
    )


def create_type_info_for_tuple_3(t0_type_info: CLTypeInfo, t1_type_info: CLTypeInfo, t2_type_info: CLTypeInfo):
    return CLTypeInfoForTuple3(
        typeof=CLType.TUPLE_1,
        t0_type_info=t0_type_info,
        t1_type_info=t1_type_info,
        t2_type_info=t2_type_info
    )
