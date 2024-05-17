# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_files.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="data_files.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x10\x64\x61ta_files.proto"\x8f\x01\n\x0cStatisticRow\x12\x0f\n\x07statval\x18\x01 \x01(\x02\x12\x1b\n\x13ordinal_by_universe\x18\x02 \x03(\x05\x12#\n\x1boverall_ordinal_by_universe\x18\x03 \x03(\x05\x12,\n$percentile_by_population_by_universe\x18\x04 \x03(\x02"F\n\rRelatedButton\x12\x10\n\x08longname\x18\x01 \x01(\t\x12\x11\n\tshortname\x18\x02 \x01(\t\x12\x10\n\x08row_type\x18\x03 \x01(\t"L\n\x0eRelatedButtons\x12\x19\n\x11relationship_type\x18\x01 \x01(\t\x12\x1f\n\x07\x62uttons\x18\x02 \x03(\x0b\x32\x0e.RelatedButton"\xa6\x01\n\x07\x41rticle\x12\x11\n\tshortname\x18\x01 \x01(\t\x12\x10\n\x08longname\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x14\n\x0c\x61rticle_type\x18\x04 \x01(\t\x12\x1b\n\x04rows\x18\x05 \x03(\x0b\x32\r.StatisticRow\x12 \n\x07related\x18\x06 \x03(\x0b\x32\x0f.RelatedButtons\x12\x11\n\tuniverses\x18\x07 \x03(\t"&\n\nCoordinate\x12\x0b\n\x03lon\x18\x01 \x01(\x02\x12\x0b\n\x03lat\x18\x02 \x01(\x02"#\n\x04Ring\x12\x1b\n\x06\x63oords\x18\x01 \x03(\x0b\x32\x0b.Coordinate"\x1f\n\x07Polygon\x12\x14\n\x05rings\x18\x01 \x03(\x0b\x32\x05.Ring"*\n\x0cMultiPolygon\x12\x1a\n\x08polygons\x18\x01 \x03(\x0b\x32\x08.Polygon"Y\n\x07\x46\x65\x61ture\x12\x1b\n\x07polygon\x18\x01 \x01(\x0b\x32\x08.PolygonH\x00\x12%\n\x0cmultipolygon\x18\x02 \x01(\x0b\x32\r.MultiPolygonH\x00\x42\n\n\x08geometry"\x1e\n\nStringList\x12\x10\n\x08\x65lements\x18\x01 \x03(\t"\x1f\n\tOrderList\x12\x12\n\norder_idxs\x18\x01 \x03(\x05"8\n\x08\x44\x61taList\x12\r\n\x05value\x18\x01 \x03(\x02\x12\x1d\n\x15population_percentile\x18\x02 \x03(\x02"\x19\n\x08\x41llStats\x12\r\n\x05stats\x18\x01 \x03(\x02"A\n\x12\x43onsolidatedShapes\x12\x11\n\tlongnames\x18\x01 \x03(\t\x12\x18\n\x06shapes\x18\x02 \x03(\x0b\x32\x08.Feature"Y\n\x16\x43onsolidatedStatistics\x12\x11\n\tlongnames\x18\x01 \x03(\t\x12\x12\n\nshortnames\x18\x02 \x03(\t\x12\x18\n\x05stats\x18\x03 \x03(\x0b\x32\t.AllStatsb\x06proto3',
)


_STATISTICROW = _descriptor.Descriptor(
    name="StatisticRow",
    full_name="StatisticRow",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="statval",
            full_name="StatisticRow.statval",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="ordinal_by_universe",
            full_name="StatisticRow.ordinal_by_universe",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="overall_ordinal_by_universe",
            full_name="StatisticRow.overall_ordinal_by_universe",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="percentile_by_population_by_universe",
            full_name="StatisticRow.percentile_by_population_by_universe",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=21,
    serialized_end=164,
)


_RELATEDBUTTON = _descriptor.Descriptor(
    name="RelatedButton",
    full_name="RelatedButton",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="longname",
            full_name="RelatedButton.longname",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="shortname",
            full_name="RelatedButton.shortname",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="row_type",
            full_name="RelatedButton.row_type",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=166,
    serialized_end=236,
)


_RELATEDBUTTONS = _descriptor.Descriptor(
    name="RelatedButtons",
    full_name="RelatedButtons",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="relationship_type",
            full_name="RelatedButtons.relationship_type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="buttons",
            full_name="RelatedButtons.buttons",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=238,
    serialized_end=314,
)


_ARTICLE = _descriptor.Descriptor(
    name="Article",
    full_name="Article",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="shortname",
            full_name="Article.shortname",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="longname",
            full_name="Article.longname",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="source",
            full_name="Article.source",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="article_type",
            full_name="Article.article_type",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="rows",
            full_name="Article.rows",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="related",
            full_name="Article.related",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="universes",
            full_name="Article.universes",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=317,
    serialized_end=483,
)


_COORDINATE = _descriptor.Descriptor(
    name="Coordinate",
    full_name="Coordinate",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="lon",
            full_name="Coordinate.lon",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="lat",
            full_name="Coordinate.lat",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=485,
    serialized_end=523,
)


_RING = _descriptor.Descriptor(
    name="Ring",
    full_name="Ring",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="coords",
            full_name="Ring.coords",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=525,
    serialized_end=560,
)


_POLYGON = _descriptor.Descriptor(
    name="Polygon",
    full_name="Polygon",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="rings",
            full_name="Polygon.rings",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=562,
    serialized_end=593,
)


_MULTIPOLYGON = _descriptor.Descriptor(
    name="MultiPolygon",
    full_name="MultiPolygon",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="polygons",
            full_name="MultiPolygon.polygons",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=595,
    serialized_end=637,
)


_FEATURE = _descriptor.Descriptor(
    name="Feature",
    full_name="Feature",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="polygon",
            full_name="Feature.polygon",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="multipolygon",
            full_name="Feature.multipolygon",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="geometry",
            full_name="Feature.geometry",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=639,
    serialized_end=728,
)


_STRINGLIST = _descriptor.Descriptor(
    name="StringList",
    full_name="StringList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="elements",
            full_name="StringList.elements",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=730,
    serialized_end=760,
)


_ORDERLIST = _descriptor.Descriptor(
    name="OrderList",
    full_name="OrderList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="order_idxs",
            full_name="OrderList.order_idxs",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=762,
    serialized_end=793,
)


_DATALIST = _descriptor.Descriptor(
    name="DataList",
    full_name="DataList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="DataList.value",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="population_percentile",
            full_name="DataList.population_percentile",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=795,
    serialized_end=851,
)


_ALLSTATS = _descriptor.Descriptor(
    name="AllStats",
    full_name="AllStats",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="stats",
            full_name="AllStats.stats",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=853,
    serialized_end=878,
)


_CONSOLIDATEDSHAPES = _descriptor.Descriptor(
    name="ConsolidatedShapes",
    full_name="ConsolidatedShapes",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="longnames",
            full_name="ConsolidatedShapes.longnames",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="shapes",
            full_name="ConsolidatedShapes.shapes",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=880,
    serialized_end=945,
)


_CONSOLIDATEDSTATISTICS = _descriptor.Descriptor(
    name="ConsolidatedStatistics",
    full_name="ConsolidatedStatistics",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="longnames",
            full_name="ConsolidatedStatistics.longnames",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="shortnames",
            full_name="ConsolidatedStatistics.shortnames",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="stats",
            full_name="ConsolidatedStatistics.stats",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=947,
    serialized_end=1036,
)

_RELATEDBUTTONS.fields_by_name["buttons"].message_type = _RELATEDBUTTON
_ARTICLE.fields_by_name["rows"].message_type = _STATISTICROW
_ARTICLE.fields_by_name["related"].message_type = _RELATEDBUTTONS
_RING.fields_by_name["coords"].message_type = _COORDINATE
_POLYGON.fields_by_name["rings"].message_type = _RING
_MULTIPOLYGON.fields_by_name["polygons"].message_type = _POLYGON
_FEATURE.fields_by_name["polygon"].message_type = _POLYGON
_FEATURE.fields_by_name["multipolygon"].message_type = _MULTIPOLYGON
_FEATURE.oneofs_by_name["geometry"].fields.append(_FEATURE.fields_by_name["polygon"])
_FEATURE.fields_by_name["polygon"].containing_oneof = _FEATURE.oneofs_by_name[
    "geometry"
]
_FEATURE.oneofs_by_name["geometry"].fields.append(
    _FEATURE.fields_by_name["multipolygon"]
)
_FEATURE.fields_by_name["multipolygon"].containing_oneof = _FEATURE.oneofs_by_name[
    "geometry"
]
_CONSOLIDATEDSHAPES.fields_by_name["shapes"].message_type = _FEATURE
_CONSOLIDATEDSTATISTICS.fields_by_name["stats"].message_type = _ALLSTATS
DESCRIPTOR.message_types_by_name["StatisticRow"] = _STATISTICROW
DESCRIPTOR.message_types_by_name["RelatedButton"] = _RELATEDBUTTON
DESCRIPTOR.message_types_by_name["RelatedButtons"] = _RELATEDBUTTONS
DESCRIPTOR.message_types_by_name["Article"] = _ARTICLE
DESCRIPTOR.message_types_by_name["Coordinate"] = _COORDINATE
DESCRIPTOR.message_types_by_name["Ring"] = _RING
DESCRIPTOR.message_types_by_name["Polygon"] = _POLYGON
DESCRIPTOR.message_types_by_name["MultiPolygon"] = _MULTIPOLYGON
DESCRIPTOR.message_types_by_name["Feature"] = _FEATURE
DESCRIPTOR.message_types_by_name["StringList"] = _STRINGLIST
DESCRIPTOR.message_types_by_name["OrderList"] = _ORDERLIST
DESCRIPTOR.message_types_by_name["DataList"] = _DATALIST
DESCRIPTOR.message_types_by_name["AllStats"] = _ALLSTATS
DESCRIPTOR.message_types_by_name["ConsolidatedShapes"] = _CONSOLIDATEDSHAPES
DESCRIPTOR.message_types_by_name["ConsolidatedStatistics"] = _CONSOLIDATEDSTATISTICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatisticRow = _reflection.GeneratedProtocolMessageType(
    "StatisticRow",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATISTICROW,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:StatisticRow)
    },
)
_sym_db.RegisterMessage(StatisticRow)

RelatedButton = _reflection.GeneratedProtocolMessageType(
    "RelatedButton",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELATEDBUTTON,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:RelatedButton)
    },
)
_sym_db.RegisterMessage(RelatedButton)

RelatedButtons = _reflection.GeneratedProtocolMessageType(
    "RelatedButtons",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELATEDBUTTONS,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:RelatedButtons)
    },
)
_sym_db.RegisterMessage(RelatedButtons)

Article = _reflection.GeneratedProtocolMessageType(
    "Article",
    (_message.Message,),
    {
        "DESCRIPTOR": _ARTICLE,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:Article)
    },
)
_sym_db.RegisterMessage(Article)

Coordinate = _reflection.GeneratedProtocolMessageType(
    "Coordinate",
    (_message.Message,),
    {
        "DESCRIPTOR": _COORDINATE,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:Coordinate)
    },
)
_sym_db.RegisterMessage(Coordinate)

Ring = _reflection.GeneratedProtocolMessageType(
    "Ring",
    (_message.Message,),
    {
        "DESCRIPTOR": _RING,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:Ring)
    },
)
_sym_db.RegisterMessage(Ring)

Polygon = _reflection.GeneratedProtocolMessageType(
    "Polygon",
    (_message.Message,),
    {
        "DESCRIPTOR": _POLYGON,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:Polygon)
    },
)
_sym_db.RegisterMessage(Polygon)

MultiPolygon = _reflection.GeneratedProtocolMessageType(
    "MultiPolygon",
    (_message.Message,),
    {
        "DESCRIPTOR": _MULTIPOLYGON,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:MultiPolygon)
    },
)
_sym_db.RegisterMessage(MultiPolygon)

Feature = _reflection.GeneratedProtocolMessageType(
    "Feature",
    (_message.Message,),
    {
        "DESCRIPTOR": _FEATURE,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:Feature)
    },
)
_sym_db.RegisterMessage(Feature)

StringList = _reflection.GeneratedProtocolMessageType(
    "StringList",
    (_message.Message,),
    {
        "DESCRIPTOR": _STRINGLIST,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:StringList)
    },
)
_sym_db.RegisterMessage(StringList)

OrderList = _reflection.GeneratedProtocolMessageType(
    "OrderList",
    (_message.Message,),
    {
        "DESCRIPTOR": _ORDERLIST,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:OrderList)
    },
)
_sym_db.RegisterMessage(OrderList)

DataList = _reflection.GeneratedProtocolMessageType(
    "DataList",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATALIST,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:DataList)
    },
)
_sym_db.RegisterMessage(DataList)

AllStats = _reflection.GeneratedProtocolMessageType(
    "AllStats",
    (_message.Message,),
    {
        "DESCRIPTOR": _ALLSTATS,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:AllStats)
    },
)
_sym_db.RegisterMessage(AllStats)

ConsolidatedShapes = _reflection.GeneratedProtocolMessageType(
    "ConsolidatedShapes",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONSOLIDATEDSHAPES,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:ConsolidatedShapes)
    },
)
_sym_db.RegisterMessage(ConsolidatedShapes)

ConsolidatedStatistics = _reflection.GeneratedProtocolMessageType(
    "ConsolidatedStatistics",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONSOLIDATEDSTATISTICS,
        "__module__": "data_files_pb2"
        # @@protoc_insertion_point(class_scope:ConsolidatedStatistics)
    },
)
_sym_db.RegisterMessage(ConsolidatedStatistics)


# @@protoc_insertion_point(module_scope)
