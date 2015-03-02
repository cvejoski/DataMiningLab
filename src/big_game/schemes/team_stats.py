# ./team_stats.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-12-29 23:57:33.515349 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:130a7f6c-8fae-11e4-a976-002710dca3dc')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sports-metadata uses Python identifier sports_metadata
    __sports_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-metadata'), 'sports_metadata', '__AbsentNamespace0_CTD_ANON_sports_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 8, 4), )

    
    sports_metadata = property(__sports_metadata.value, __sports_metadata.set, None, None)

    
    # Element sports-event uses Python identifier sports_event
    __sports_event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-event'), 'sports_event', '__AbsentNamespace0_CTD_ANON_sports_event', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 20, 4), )

    
    sports_event = property(__sports_event.value, __sports_event.set, None, None)

    _ElementMap.update({
        __sports_metadata.name() : __sports_metadata,
        __sports_event.name() : __sports_event
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 9, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sports-title uses Python identifier sports_title
    __sports_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-title'), 'sports_title', '__AbsentNamespace0_CTD_ANON__sports_title', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 11, 7), )

    
    sports_title = property(__sports_title.value, __sports_title.set, None, None)

    
    # Attribute doc-id uses Python identifier doc_id
    __doc_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'doc-id'), 'doc_id', '__AbsentNamespace0_CTD_ANON__doc_id', pyxb.binding.datatypes.string)
    __doc_id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 13, 6)
    __doc_id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 13, 6)
    
    doc_id = property(__doc_id.value, __doc_id.set, None, None)

    
    # Attribute date-time uses Python identifier date_time
    __date_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-time'), 'date_time', '__AbsentNamespace0_CTD_ANON__date_time', pyxb.binding.datatypes.string)
    __date_time._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 14, 6)
    __date_time._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 14, 6)
    
    date_time = property(__date_time.value, __date_time.set, None, None)

    
    # Attribute publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publisher'), 'publisher', '__AbsentNamespace0_CTD_ANON__publisher', pyxb.binding.datatypes.string)
    __publisher._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 15, 6)
    __publisher._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 15, 6)
    
    publisher = property(__publisher.value, __publisher.set, None, None)

    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'language'), 'language', '__AbsentNamespace0_CTD_ANON__language', pyxb.binding.datatypes.string)
    __language._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 16, 6)
    __language._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 16, 6)
    
    language = property(__language.value, __language.set, None, None)

    
    # Attribute document-class uses Python identifier document_class
    __document_class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'document-class'), 'document_class', '__AbsentNamespace0_CTD_ANON__document_class', pyxb.binding.datatypes.string)
    __document_class._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 17, 6)
    __document_class._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 17, 6)
    
    document_class = property(__document_class.value, __document_class.set, None, None)

    _ElementMap.update({
        __sports_title.name() : __sports_title
    })
    _AttributeMap.update({
        __doc_id.name() : __doc_id,
        __date_time.name() : __date_time,
        __publisher.name() : __publisher,
        __language.name() : __language,
        __document_class.name() : __document_class
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 21, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element event-metadata uses Python identifier event_metadata
    __event_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'event-metadata'), 'event_metadata', '__AbsentNamespace0_CTD_ANON_2_event_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 23, 7), )

    
    event_metadata = property(__event_metadata.value, __event_metadata.set, None, None)

    
    # Element team uses Python identifier team
    __team = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team'), 'team', '__AbsentNamespace0_CTD_ANON_2_team', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 34, 7), )

    
    team = property(__team.value, __team.set, None, None)

    _ElementMap.update({
        __event_metadata.name() : __event_metadata,
        __team.name() : __team
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 24, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_3_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 25, 9)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 25, 9)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute event-key uses Python identifier event_key
    __event_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'event-key'), 'event_key', '__AbsentNamespace0_CTD_ANON_3_event_key', pyxb.binding.datatypes.int)
    __event_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 26, 9)
    __event_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 26, 9)
    
    event_key = property(__event_key.value, __event_key.set, None, None)

    
    # Attribute event-status uses Python identifier event_status
    __event_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'event-status'), 'event_status', '__AbsentNamespace0_CTD_ANON_3_event_status', pyxb.binding.datatypes.string)
    __event_status._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 27, 9)
    __event_status._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 27, 9)
    
    event_status = property(__event_status.value, __event_status.set, None, None)

    
    # Attribute start-date-time uses Python identifier start_date_time
    __start_date_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-date-time'), 'start_date_time', '__AbsentNamespace0_CTD_ANON_3_start_date_time', pyxb.binding.datatypes.string)
    __start_date_time._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 28, 9)
    __start_date_time._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 28, 9)
    
    start_date_time = property(__start_date_time.value, __start_date_time.set, None, None)

    
    # Attribute start-weekday uses Python identifier start_weekday
    __start_weekday = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-weekday'), 'start_weekday', '__AbsentNamespace0_CTD_ANON_3_start_weekday', pyxb.binding.datatypes.string)
    __start_weekday._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 29, 9)
    __start_weekday._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 29, 9)
    
    start_weekday = property(__start_weekday.value, __start_weekday.set, None, None)

    
    # Attribute heat-number uses Python identifier heat_number
    __heat_number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'heat-number'), 'heat_number', '__AbsentNamespace0_CTD_ANON_3_heat_number', pyxb.binding.datatypes.int)
    __heat_number._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 30, 9)
    __heat_number._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 30, 9)
    
    heat_number = property(__heat_number.value, __heat_number.set, None, None)

    
    # Attribute site-attendance uses Python identifier site_attendance
    __site_attendance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'site-attendance'), 'site_attendance', '__AbsentNamespace0_CTD_ANON_3_site_attendance', pyxb.binding.datatypes.int)
    __site_attendance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 31, 9)
    __site_attendance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 31, 9)
    
    site_attendance = property(__site_attendance.value, __site_attendance.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __event_key.name() : __event_key,
        __event_status.name() : __event_status,
        __start_date_time.name() : __start_date_time,
        __start_weekday.name() : __start_weekday,
        __heat_number.name() : __heat_number,
        __site_attendance.name() : __site_attendance
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 35, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element team-metadata uses Python identifier team_metadata
    __team_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team-metadata'), 'team_metadata', '__AbsentNamespace0_CTD_ANON_4_team_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 37, 10), )

    
    team_metadata = property(__team_metadata.value, __team_metadata.set, None, None)

    
    # Element team-stats uses Python identifier team_stats
    __team_stats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team-stats'), 'team_stats', '__AbsentNamespace0_CTD_ANON_4_team_stats', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 53, 10), )

    
    team_stats = property(__team_stats.value, __team_stats.set, None, None)

    
    # Element team-stats-tracking uses Python identifier team_stats_tracking
    __team_stats_tracking = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team-stats-tracking'), 'team_stats_tracking', '__AbsentNamespace0_CTD_ANON_4_team_stats_tracking', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 115, 10), )

    
    team_stats_tracking = property(__team_stats_tracking.value, __team_stats_tracking.set, None, None)

    _ElementMap.update({
        __team_metadata.name() : __team_metadata,
        __team_stats.name() : __team_stats,
        __team_stats_tracking.name() : __team_stats_tracking
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 38, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_5_name', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 40, 13), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_5_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 47, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 47, 12)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute team-key uses Python identifier team_key
    __team_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'team-key'), 'team_key', '__AbsentNamespace0_CTD_ANON_5_team_key', pyxb.binding.datatypes.int)
    __team_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 48, 12)
    __team_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 48, 12)
    
    team_key = property(__team_key.value, __team_key.set, None, None)

    
    # Attribute alignment uses Python identifier alignment
    __alignment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alignment'), 'alignment', '__AbsentNamespace0_CTD_ANON_5_alignment', pyxb.binding.datatypes.string)
    __alignment._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 49, 12)
    __alignment._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 49, 12)
    
    alignment = property(__alignment.value, __alignment.set, None, None)

    
    # Attribute average-age uses Python identifier average_age
    __average_age = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'average-age'), 'average_age', '__AbsentNamespace0_CTD_ANON_5_average_age', pyxb.binding.datatypes.double)
    __average_age._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 50, 12)
    __average_age._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 50, 12)
    
    average_age = property(__average_age.value, __average_age.set, None, None)

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __id.name() : __id,
        __team_key.name() : __team_key,
        __alignment.name() : __alignment,
        __average_age.name() : __average_age
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 41, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__AbsentNamespace0_CTD_ANON_6_full', pyxb.binding.datatypes.string)
    __full._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 42, 15)
    __full._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 42, 15)
    
    full = property(__full.value, __full.set, None, None)

    
    # Attribute nickname uses Python identifier nickname
    __nickname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nickname'), 'nickname', '__AbsentNamespace0_CTD_ANON_6_nickname', pyxb.binding.datatypes.string)
    __nickname._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 43, 15)
    __nickname._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 43, 15)
    
    nickname = property(__nickname.value, __nickname.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __full.name() : __full,
        __nickname.name() : __nickname
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 54, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element team-stats-soccer uses Python identifier team_stats_soccer
    __team_stats_soccer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team-stats-soccer'), 'team_stats_soccer', '__AbsentNamespace0_CTD_ANON_7_team_stats_soccer', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 56, 13), )

    
    team_stats_soccer = property(__team_stats_soccer.value, __team_stats_soccer.set, None, None)

    
    # Attribute date-coverage-type uses Python identifier date_coverage_type
    __date_coverage_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-coverage-type'), 'date_coverage_type', '__AbsentNamespace0_CTD_ANON_7_date_coverage_type', pyxb.binding.datatypes.string)
    __date_coverage_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 109, 12)
    __date_coverage_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 109, 12)
    
    date_coverage_type = property(__date_coverage_type.value, __date_coverage_type.set, None, None)

    
    # Attribute date-coverage-value uses Python identifier date_coverage_value
    __date_coverage_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-coverage-value'), 'date_coverage_value', '__AbsentNamespace0_CTD_ANON_7_date_coverage_value', pyxb.binding.datatypes.string)
    __date_coverage_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 110, 12)
    __date_coverage_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 110, 12)
    
    date_coverage_value = property(__date_coverage_value.value, __date_coverage_value.set, None, None)

    
    # Attribute period-value uses Python identifier period_value
    __period_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-value'), 'period_value', '__AbsentNamespace0_CTD_ANON_7_period_value', pyxb.binding.datatypes.int)
    __period_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 111, 12)
    __period_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 111, 12)
    
    period_value = property(__period_value.value, __period_value.set, None, None)

    
    # Attribute score uses Python identifier score
    __score = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score'), 'score', '__AbsentNamespace0_CTD_ANON_7_score', pyxb.binding.datatypes.int)
    __score._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 112, 12)
    __score._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 112, 12)
    
    score = property(__score.value, __score.set, None, None)

    _ElementMap.update({
        __team_stats_soccer.name() : __team_stats_soccer
    })
    _AttributeMap.update({
        __date_coverage_type.name() : __date_coverage_type,
        __date_coverage_value.name() : __date_coverage_value,
        __period_value.name() : __period_value,
        __score.name() : __score
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 57, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element stats-soccer-offensive uses Python identifier stats_soccer_offensive
    __stats_soccer_offensive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-soccer-offensive'), 'stats_soccer_offensive', '__AbsentNamespace0_CTD_ANON_8_stats_soccer_offensive', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 59, 16), )

    
    stats_soccer_offensive = property(__stats_soccer_offensive.value, __stats_soccer_offensive.set, None, None)

    
    # Element stats-soccer-defensive uses Python identifier stats_soccer_defensive
    __stats_soccer_defensive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-soccer-defensive'), 'stats_soccer_defensive', '__AbsentNamespace0_CTD_ANON_8_stats_soccer_defensive', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 78, 16), )

    
    stats_soccer_defensive = property(__stats_soccer_defensive.value, __stats_soccer_defensive.set, None, None)

    
    # Element stats-soccer-foul uses Python identifier stats_soccer_foul
    __stats_soccer_foul = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-soccer-foul'), 'stats_soccer_foul', '__AbsentNamespace0_CTD_ANON_8_stats_soccer_foul', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 83, 16), )

    
    stats_soccer_foul = property(__stats_soccer_foul.value, __stats_soccer_foul.set, None, None)

    
    # Attribute duels-won uses Python identifier duels_won
    __duels_won = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-won'), 'duels_won', '__AbsentNamespace0_CTD_ANON_8_duels_won', pyxb.binding.datatypes.int)
    __duels_won._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 94, 15)
    __duels_won._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 94, 15)
    
    duels_won = property(__duels_won.value, __duels_won.set, None, None)

    
    # Attribute duels-lost uses Python identifier duels_lost
    __duels_lost = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-lost'), 'duels_lost', '__AbsentNamespace0_CTD_ANON_8_duels_lost', pyxb.binding.datatypes.int)
    __duels_lost._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 95, 15)
    __duels_lost._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 95, 15)
    
    duels_lost = property(__duels_lost.value, __duels_lost.set, None, None)

    
    # Attribute duels-won-percentage uses Python identifier duels_won_percentage
    __duels_won_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-won-percentage'), 'duels_won_percentage', '__AbsentNamespace0_CTD_ANON_8_duels_won_percentage', pyxb.binding.datatypes.double)
    __duels_won_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 96, 15)
    __duels_won_percentage._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 96, 15)
    
    duels_won_percentage = property(__duels_won_percentage.value, __duels_won_percentage.set, None, None)

    
    # Attribute passes-completed uses Python identifier passes_completed
    __passes_completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes-completed'), 'passes_completed', '__AbsentNamespace0_CTD_ANON_8_passes_completed', pyxb.binding.datatypes.int)
    __passes_completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 97, 15)
    __passes_completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 97, 15)
    
    passes_completed = property(__passes_completed.value, __passes_completed.set, None, None)

    
    # Attribute passes-failed uses Python identifier passes_failed
    __passes_failed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes-failed'), 'passes_failed', '__AbsentNamespace0_CTD_ANON_8_passes_failed', pyxb.binding.datatypes.int)
    __passes_failed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 98, 15)
    __passes_failed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 98, 15)
    
    passes_failed = property(__passes_failed.value, __passes_failed.set, None, None)

    
    # Attribute passes-completions-percentage uses Python identifier passes_completions_percentage
    __passes_completions_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes-completions-percentage'), 'passes_completions_percentage', '__AbsentNamespace0_CTD_ANON_8_passes_completions_percentage', pyxb.binding.datatypes.double)
    __passes_completions_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 99, 15)
    __passes_completions_percentage._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 99, 15)
    
    passes_completions_percentage = property(__passes_completions_percentage.value, __passes_completions_percentage.set, None, None)

    
    # Attribute passes-failed-percentage uses Python identifier passes_failed_percentage
    __passes_failed_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes-failed-percentage'), 'passes_failed_percentage', '__AbsentNamespace0_CTD_ANON_8_passes_failed_percentage', pyxb.binding.datatypes.double)
    __passes_failed_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 100, 15)
    __passes_failed_percentage._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 100, 15)
    
    passes_failed_percentage = property(__passes_failed_percentage.value, __passes_failed_percentage.set, None, None)

    
    # Attribute balls-touched uses Python identifier balls_touched
    __balls_touched = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'balls-touched'), 'balls_touched', '__AbsentNamespace0_CTD_ANON_8_balls_touched', pyxb.binding.datatypes.int)
    __balls_touched._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 101, 15)
    __balls_touched._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 101, 15)
    
    balls_touched = property(__balls_touched.value, __balls_touched.set, None, None)

    
    # Attribute balls-touched-percentage uses Python identifier balls_touched_percentage
    __balls_touched_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'balls-touched-percentage'), 'balls_touched_percentage', '__AbsentNamespace0_CTD_ANON_8_balls_touched_percentage', pyxb.binding.datatypes.double)
    __balls_touched_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 102, 15)
    __balls_touched_percentage._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 102, 15)
    
    balls_touched_percentage = property(__balls_touched_percentage.value, __balls_touched_percentage.set, None, None)

    
    # Attribute tracking-distance uses Python identifier tracking_distance
    __tracking_distance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-distance'), 'tracking_distance', '__AbsentNamespace0_CTD_ANON_8_tracking_distance', pyxb.binding.datatypes.double)
    __tracking_distance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 103, 15)
    __tracking_distance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 103, 15)
    
    tracking_distance = property(__tracking_distance.value, __tracking_distance.set, None, None)

    
    # Attribute tracking-sprints uses Python identifier tracking_sprints
    __tracking_sprints = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-sprints'), 'tracking_sprints', '__AbsentNamespace0_CTD_ANON_8_tracking_sprints', pyxb.binding.datatypes.int)
    __tracking_sprints._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 104, 15)
    __tracking_sprints._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 104, 15)
    
    tracking_sprints = property(__tracking_sprints.value, __tracking_sprints.set, None, None)

    
    # Attribute tracking-fast-runs uses Python identifier tracking_fast_runs
    __tracking_fast_runs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-fast-runs'), 'tracking_fast_runs', '__AbsentNamespace0_CTD_ANON_8_tracking_fast_runs', pyxb.binding.datatypes.int)
    __tracking_fast_runs._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 105, 15)
    __tracking_fast_runs._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 105, 15)
    
    tracking_fast_runs = property(__tracking_fast_runs.value, __tracking_fast_runs.set, None, None)

    _ElementMap.update({
        __stats_soccer_offensive.name() : __stats_soccer_offensive,
        __stats_soccer_defensive.name() : __stats_soccer_defensive,
        __stats_soccer_foul.name() : __stats_soccer_foul
    })
    _AttributeMap.update({
        __duels_won.name() : __duels_won,
        __duels_lost.name() : __duels_lost,
        __duels_won_percentage.name() : __duels_won_percentage,
        __passes_completed.name() : __passes_completed,
        __passes_failed.name() : __passes_failed,
        __passes_completions_percentage.name() : __passes_completions_percentage,
        __passes_failed_percentage.name() : __passes_failed_percentage,
        __balls_touched.name() : __balls_touched,
        __balls_touched_percentage.name() : __balls_touched_percentage,
        __tracking_distance.name() : __tracking_distance,
        __tracking_sprints.name() : __tracking_sprints,
        __tracking_fast_runs.name() : __tracking_fast_runs
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 60, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute shots-total uses Python identifier shots_total
    __shots_total = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-total'), 'shots_total', '__AbsentNamespace0_CTD_ANON_9_shots_total', pyxb.binding.datatypes.int)
    __shots_total._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 61, 18)
    __shots_total._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 61, 18)
    
    shots_total = property(__shots_total.value, __shots_total.set, None, None)

    
    # Attribute shots-on-goal-total uses Python identifier shots_on_goal_total
    __shots_on_goal_total = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-on-goal-total'), 'shots_on_goal_total', '__AbsentNamespace0_CTD_ANON_9_shots_on_goal_total', pyxb.binding.datatypes.int)
    __shots_on_goal_total._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 62, 18)
    __shots_on_goal_total._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 62, 18)
    
    shots_on_goal_total = property(__shots_on_goal_total.value, __shots_on_goal_total.set, None, None)

    
    # Attribute offsides uses Python identifier offsides
    __offsides = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offsides'), 'offsides', '__AbsentNamespace0_CTD_ANON_9_offsides', pyxb.binding.datatypes.int)
    __offsides._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 63, 18)
    __offsides._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 63, 18)
    
    offsides = property(__offsides.value, __offsides.set, None, None)

    
    # Attribute corner-kicks uses Python identifier corner_kicks
    __corner_kicks = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'corner-kicks'), 'corner_kicks', '__AbsentNamespace0_CTD_ANON_9_corner_kicks', pyxb.binding.datatypes.int)
    __corner_kicks._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 64, 18)
    __corner_kicks._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 64, 18)
    
    corner_kicks = property(__corner_kicks.value, __corner_kicks.set, None, None)

    
    # Attribute corner-kicks-left uses Python identifier corner_kicks_left
    __corner_kicks_left = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'corner-kicks-left'), 'corner_kicks_left', '__AbsentNamespace0_CTD_ANON_9_corner_kicks_left', pyxb.binding.datatypes.int)
    __corner_kicks_left._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 65, 18)
    __corner_kicks_left._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 65, 18)
    
    corner_kicks_left = property(__corner_kicks_left.value, __corner_kicks_left.set, None, None)

    
    # Attribute corner-kicks-right uses Python identifier corner_kicks_right
    __corner_kicks_right = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'corner-kicks-right'), 'corner_kicks_right', '__AbsentNamespace0_CTD_ANON_9_corner_kicks_right', pyxb.binding.datatypes.int)
    __corner_kicks_right._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 66, 18)
    __corner_kicks_right._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 66, 18)
    
    corner_kicks_right = property(__corner_kicks_right.value, __corner_kicks_right.set, None, None)

    
    # Attribute shots-total-outside-box uses Python identifier shots_total_outside_box
    __shots_total_outside_box = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-total-outside-box'), 'shots_total_outside_box', '__AbsentNamespace0_CTD_ANON_9_shots_total_outside_box', pyxb.binding.datatypes.int)
    __shots_total_outside_box._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 67, 18)
    __shots_total_outside_box._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 67, 18)
    
    shots_total_outside_box = property(__shots_total_outside_box.value, __shots_total_outside_box.set, None, None)

    
    # Attribute shots-total-inside-box uses Python identifier shots_total_inside_box
    __shots_total_inside_box = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-total-inside-box'), 'shots_total_inside_box', '__AbsentNamespace0_CTD_ANON_9_shots_total_inside_box', pyxb.binding.datatypes.int)
    __shots_total_inside_box._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 68, 18)
    __shots_total_inside_box._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 68, 18)
    
    shots_total_inside_box = property(__shots_total_inside_box.value, __shots_total_inside_box.set, None, None)

    
    # Attribute shots-foot-inside-box uses Python identifier shots_foot_inside_box
    __shots_foot_inside_box = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-foot-inside-box'), 'shots_foot_inside_box', '__AbsentNamespace0_CTD_ANON_9_shots_foot_inside_box', pyxb.binding.datatypes.int)
    __shots_foot_inside_box._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 69, 18)
    __shots_foot_inside_box._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 69, 18)
    
    shots_foot_inside_box = property(__shots_foot_inside_box.value, __shots_foot_inside_box.set, None, None)

    
    # Attribute shots-foot-outside-box uses Python identifier shots_foot_outside_box
    __shots_foot_outside_box = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-foot-outside-box'), 'shots_foot_outside_box', '__AbsentNamespace0_CTD_ANON_9_shots_foot_outside_box', pyxb.binding.datatypes.int)
    __shots_foot_outside_box._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 70, 18)
    __shots_foot_outside_box._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 70, 18)
    
    shots_foot_outside_box = property(__shots_foot_outside_box.value, __shots_foot_outside_box.set, None, None)

    
    # Attribute shots-total-header uses Python identifier shots_total_header
    __shots_total_header = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-total-header'), 'shots_total_header', '__AbsentNamespace0_CTD_ANON_9_shots_total_header', pyxb.binding.datatypes.int)
    __shots_total_header._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 71, 18)
    __shots_total_header._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 71, 18)
    
    shots_total_header = property(__shots_total_header.value, __shots_total_header.set, None, None)

    
    # Attribute crosses uses Python identifier crosses
    __crosses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crosses'), 'crosses', '__AbsentNamespace0_CTD_ANON_9_crosses', pyxb.binding.datatypes.int)
    __crosses._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 72, 18)
    __crosses._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 72, 18)
    
    crosses = property(__crosses.value, __crosses.set, None, None)

    
    # Attribute crosses-left uses Python identifier crosses_left
    __crosses_left = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crosses-left'), 'crosses_left', '__AbsentNamespace0_CTD_ANON_9_crosses_left', pyxb.binding.datatypes.int)
    __crosses_left._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 73, 18)
    __crosses_left._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 73, 18)
    
    crosses_left = property(__crosses_left.value, __crosses_left.set, None, None)

    
    # Attribute crosses-right uses Python identifier crosses_right
    __crosses_right = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crosses-right'), 'crosses_right', '__AbsentNamespace0_CTD_ANON_9_crosses_right', pyxb.binding.datatypes.int)
    __crosses_right._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 74, 18)
    __crosses_right._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 74, 18)
    
    crosses_right = property(__crosses_right.value, __crosses_right.set, None, None)

    
    # Attribute freekicks uses Python identifier freekicks
    __freekicks = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'freekicks'), 'freekicks', '__AbsentNamespace0_CTD_ANON_9_freekicks', pyxb.binding.datatypes.int)
    __freekicks._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 75, 18)
    __freekicks._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 75, 18)
    
    freekicks = property(__freekicks.value, __freekicks.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __shots_total.name() : __shots_total,
        __shots_on_goal_total.name() : __shots_on_goal_total,
        __offsides.name() : __offsides,
        __corner_kicks.name() : __corner_kicks,
        __corner_kicks_left.name() : __corner_kicks_left,
        __corner_kicks_right.name() : __corner_kicks_right,
        __shots_total_outside_box.name() : __shots_total_outside_box,
        __shots_total_inside_box.name() : __shots_total_inside_box,
        __shots_foot_inside_box.name() : __shots_foot_inside_box,
        __shots_foot_outside_box.name() : __shots_foot_outside_box,
        __shots_total_header.name() : __shots_total_header,
        __crosses.name() : __crosses,
        __crosses_left.name() : __crosses_left,
        __crosses_right.name() : __crosses_right,
        __freekicks.name() : __freekicks
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 79, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute saves uses Python identifier saves
    __saves = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'saves'), 'saves', '__AbsentNamespace0_CTD_ANON_10_saves', pyxb.binding.datatypes.int)
    __saves._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 80, 18)
    __saves._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 80, 18)
    
    saves = property(__saves.value, __saves.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __saves.name() : __saves
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 84, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fouls-suffered uses Python identifier fouls_suffered
    __fouls_suffered = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fouls-suffered'), 'fouls_suffered', '__AbsentNamespace0_CTD_ANON_11_fouls_suffered', pyxb.binding.datatypes.int)
    __fouls_suffered._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 85, 18)
    __fouls_suffered._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 85, 18)
    
    fouls_suffered = property(__fouls_suffered.value, __fouls_suffered.set, None, None)

    
    # Attribute fouls-committed uses Python identifier fouls_committed
    __fouls_committed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fouls-committed'), 'fouls_committed', '__AbsentNamespace0_CTD_ANON_11_fouls_committed', pyxb.binding.datatypes.int)
    __fouls_committed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 86, 18)
    __fouls_committed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 86, 18)
    
    fouls_committed = property(__fouls_committed.value, __fouls_committed.set, None, None)

    
    # Attribute yellow-cards uses Python identifier yellow_cards
    __yellow_cards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'yellow-cards'), 'yellow_cards', '__AbsentNamespace0_CTD_ANON_11_yellow_cards', pyxb.binding.datatypes.int)
    __yellow_cards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 87, 18)
    __yellow_cards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 87, 18)
    
    yellow_cards = property(__yellow_cards.value, __yellow_cards.set, None, None)

    
    # Attribute red-cards uses Python identifier red_cards
    __red_cards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'red-cards'), 'red_cards', '__AbsentNamespace0_CTD_ANON_11_red_cards', pyxb.binding.datatypes.int)
    __red_cards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 88, 18)
    __red_cards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 88, 18)
    
    red_cards = property(__red_cards.value, __red_cards.set, None, None)

    
    # Attribute yellow-red-cards uses Python identifier yellow_red_cards
    __yellow_red_cards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'yellow-red-cards'), 'yellow_red_cards', '__AbsentNamespace0_CTD_ANON_11_yellow_red_cards', pyxb.binding.datatypes.int)
    __yellow_red_cards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 89, 18)
    __yellow_red_cards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 89, 18)
    
    yellow_red_cards = property(__yellow_red_cards.value, __yellow_red_cards.set, None, None)

    
    # Attribute handballs uses Python identifier handballs
    __handballs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handballs'), 'handballs', '__AbsentNamespace0_CTD_ANON_11_handballs', pyxb.binding.datatypes.int)
    __handballs._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 90, 18)
    __handballs._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 90, 18)
    
    handballs = property(__handballs.value, __handballs.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fouls_suffered.name() : __fouls_suffered,
        __fouls_committed.name() : __fouls_committed,
        __yellow_cards.name() : __yellow_cards,
        __red_cards.name() : __red_cards,
        __yellow_red_cards.name() : __yellow_red_cards,
        __handballs.name() : __handballs
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 116, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element stats-time uses Python identifier stats_time
    __stats_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-time'), 'stats_time', '__AbsentNamespace0_CTD_ANON_12_stats_time', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 118, 13), )

    
    stats_time = property(__stats_time.value, __stats_time.set, None, None)

    
    # Element stats-ball uses Python identifier stats_ball
    __stats_ball = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-ball'), 'stats_ball', '__AbsentNamespace0_CTD_ANON_12_stats_ball', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 123, 13), )

    
    stats_ball = property(__stats_ball.value, __stats_ball.set, None, None)

    
    # Element stats-position uses Python identifier stats_position
    __stats_position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-position'), 'stats_position', '__AbsentNamespace0_CTD_ANON_12_stats_position', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 137, 13), )

    
    stats_position = property(__stats_position.value, __stats_position.set, None, None)

    _ElementMap.update({
        __stats_time.name() : __stats_time,
        __stats_ball.name() : __stats_ball,
        __stats_position.name() : __stats_position
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 119, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute playedTime uses Python identifier playedTime
    __playedTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playedTime'), 'playedTime', '__AbsentNamespace0_CTD_ANON_13_playedTime', pyxb.binding.datatypes.double)
    __playedTime._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 120, 15)
    __playedTime._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 120, 15)
    
    playedTime = property(__playedTime.value, __playedTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __playedTime.name() : __playedTime
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 124, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ballPossessionTime uses Python identifier ballPossessionTime
    __ballPossessionTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballPossessionTime'), 'ballPossessionTime', '__AbsentNamespace0_CTD_ANON_14_ballPossessionTime', pyxb.binding.datatypes.double)
    __ballPossessionTime._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 125, 15)
    __ballPossessionTime._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 125, 15)
    
    ballPossessionTime = property(__ballPossessionTime.value, __ballPossessionTime.set, None, None)

    
    # Attribute ballPossessionTime_OwnHalf uses Python identifier ballPossessionTime_OwnHalf
    __ballPossessionTime_OwnHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballPossessionTime_OwnHalf'), 'ballPossessionTime_OwnHalf', '__AbsentNamespace0_CTD_ANON_14_ballPossessionTime_OwnHalf', pyxb.binding.datatypes.double)
    __ballPossessionTime_OwnHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 126, 15)
    __ballPossessionTime_OwnHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 126, 15)
    
    ballPossessionTime_OwnHalf = property(__ballPossessionTime_OwnHalf.value, __ballPossessionTime_OwnHalf.set, None, None)

    
    # Attribute ballPossessionTime_OpposingHalf uses Python identifier ballPossessionTime_OpposingHalf
    __ballPossessionTime_OpposingHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballPossessionTime_OpposingHalf'), 'ballPossessionTime_OpposingHalf', '__AbsentNamespace0_CTD_ANON_14_ballPossessionTime_OpposingHalf', pyxb.binding.datatypes.double)
    __ballPossessionTime_OpposingHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 127, 15)
    __ballPossessionTime_OpposingHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 127, 15)
    
    ballPossessionTime_OpposingHalf = property(__ballPossessionTime_OpposingHalf.value, __ballPossessionTime_OpposingHalf.set, None, None)

    
    # Attribute ballInOwnHalf uses Python identifier ballInOwnHalf
    __ballInOwnHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballInOwnHalf'), 'ballInOwnHalf', '__AbsentNamespace0_CTD_ANON_14_ballInOwnHalf', pyxb.binding.datatypes.double)
    __ballInOwnHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 128, 15)
    __ballInOwnHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 128, 15)
    
    ballInOwnHalf = property(__ballInOwnHalf.value, __ballInOwnHalf.set, None, None)

    
    # Attribute ballInOpposingHalf uses Python identifier ballInOpposingHalf
    __ballInOpposingHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballInOpposingHalf'), 'ballInOpposingHalf', '__AbsentNamespace0_CTD_ANON_14_ballInOpposingHalf', pyxb.binding.datatypes.double)
    __ballInOpposingHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 129, 15)
    __ballInOpposingHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 129, 15)
    
    ballInOpposingHalf = property(__ballInOpposingHalf.value, __ballInOpposingHalf.set, None, None)

    
    # Attribute numberOfBallPossesions uses Python identifier numberOfBallPossesions
    __numberOfBallPossesions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfBallPossesions'), 'numberOfBallPossesions', '__AbsentNamespace0_CTD_ANON_14_numberOfBallPossesions', pyxb.binding.datatypes.int)
    __numberOfBallPossesions._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 130, 15)
    __numberOfBallPossesions._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 130, 15)
    
    numberOfBallPossesions = property(__numberOfBallPossesions.value, __numberOfBallPossesions.set, None, None)

    
    # Attribute numberOfOpponentBallPossesions uses Python identifier numberOfOpponentBallPossesions
    __numberOfOpponentBallPossesions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfOpponentBallPossesions'), 'numberOfOpponentBallPossesions', '__AbsentNamespace0_CTD_ANON_14_numberOfOpponentBallPossesions', pyxb.binding.datatypes.int)
    __numberOfOpponentBallPossesions._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 131, 15)
    __numberOfOpponentBallPossesions._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 131, 15)
    
    numberOfOpponentBallPossesions = property(__numberOfOpponentBallPossesions.value, __numberOfOpponentBallPossesions.set, None, None)

    
    # Attribute numberOfBallPossesionsToScoreAttempt uses Python identifier numberOfBallPossesionsToScoreAttempt
    __numberOfBallPossesionsToScoreAttempt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfBallPossesionsToScoreAttempt'), 'numberOfBallPossesionsToScoreAttempt', '__AbsentNamespace0_CTD_ANON_14_numberOfBallPossesionsToScoreAttempt', pyxb.binding.datatypes.double)
    __numberOfBallPossesionsToScoreAttempt._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 132, 15)
    __numberOfBallPossesionsToScoreAttempt._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 132, 15)
    
    numberOfBallPossesionsToScoreAttempt = property(__numberOfBallPossesionsToScoreAttempt.value, __numberOfBallPossesionsToScoreAttempt.set, None, None)

    
    # Attribute timeOfBallPossesionsToScoreAttempt uses Python identifier timeOfBallPossesionsToScoreAttempt
    __timeOfBallPossesionsToScoreAttempt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeOfBallPossesionsToScoreAttempt'), 'timeOfBallPossesionsToScoreAttempt', '__AbsentNamespace0_CTD_ANON_14_timeOfBallPossesionsToScoreAttempt', pyxb.binding.datatypes.double)
    __timeOfBallPossesionsToScoreAttempt._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 133, 15)
    __timeOfBallPossesionsToScoreAttempt._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 133, 15)
    
    timeOfBallPossesionsToScoreAttempt = property(__timeOfBallPossesionsToScoreAttempt.value, __timeOfBallPossesionsToScoreAttempt.set, None, None)

    
    # Attribute numberOfBallCaptures_OwnHalf uses Python identifier numberOfBallCaptures_OwnHalf
    __numberOfBallCaptures_OwnHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfBallCaptures_OwnHalf'), 'numberOfBallCaptures_OwnHalf', '__AbsentNamespace0_CTD_ANON_14_numberOfBallCaptures_OwnHalf', pyxb.binding.datatypes.int)
    __numberOfBallCaptures_OwnHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 134, 15)
    __numberOfBallCaptures_OwnHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 134, 15)
    
    numberOfBallCaptures_OwnHalf = property(__numberOfBallCaptures_OwnHalf.value, __numberOfBallCaptures_OwnHalf.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ballPossessionTime.name() : __ballPossessionTime,
        __ballPossessionTime_OwnHalf.name() : __ballPossessionTime_OwnHalf,
        __ballPossessionTime_OpposingHalf.name() : __ballPossessionTime_OpposingHalf,
        __ballInOwnHalf.name() : __ballInOwnHalf,
        __ballInOpposingHalf.name() : __ballInOpposingHalf,
        __numberOfBallPossesions.name() : __numberOfBallPossesions,
        __numberOfOpponentBallPossesions.name() : __numberOfOpponentBallPossesions,
        __numberOfBallPossesionsToScoreAttempt.name() : __numberOfBallPossesionsToScoreAttempt,
        __timeOfBallPossesionsToScoreAttempt.name() : __timeOfBallPossesionsToScoreAttempt,
        __numberOfBallCaptures_OwnHalf.name() : __numberOfBallCaptures_OwnHalf
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 138, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute avgDistance_AllOutfieldPlayers uses Python identifier avgDistance_AllOutfieldPlayers
    __avgDistance_AllOutfieldPlayers = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_AllOutfieldPlayers'), 'avgDistance_AllOutfieldPlayers', '__AbsentNamespace0_CTD_ANON_15_avgDistance_AllOutfieldPlayers', pyxb.binding.datatypes.double)
    __avgDistance_AllOutfieldPlayers._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 139, 15)
    __avgDistance_AllOutfieldPlayers._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 139, 15)
    
    avgDistance_AllOutfieldPlayers = property(__avgDistance_AllOutfieldPlayers.value, __avgDistance_AllOutfieldPlayers.set, None, None)

    
    # Attribute avgDistance_AllOutfieldPlayers_BallInPossesion uses Python identifier avgDistance_AllOutfieldPlayers_BallInPossesion
    __avgDistance_AllOutfieldPlayers_BallInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_AllOutfieldPlayers_BallInPossesion'), 'avgDistance_AllOutfieldPlayers_BallInPossesion', '__AbsentNamespace0_CTD_ANON_15_avgDistance_AllOutfieldPlayers_BallInPossesion', pyxb.binding.datatypes.double)
    __avgDistance_AllOutfieldPlayers_BallInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 140, 15)
    __avgDistance_AllOutfieldPlayers_BallInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 140, 15)
    
    avgDistance_AllOutfieldPlayers_BallInPossesion = property(__avgDistance_AllOutfieldPlayers_BallInPossesion.value, __avgDistance_AllOutfieldPlayers_BallInPossesion.set, None, None)

    
    # Attribute avgDistance_AllOutfieldPlayers_BallNotInPossesion uses Python identifier avgDistance_AllOutfieldPlayers_BallNotInPossesion
    __avgDistance_AllOutfieldPlayers_BallNotInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_AllOutfieldPlayers_BallNotInPossesion'), 'avgDistance_AllOutfieldPlayers_BallNotInPossesion', '__AbsentNamespace0_CTD_ANON_15_avgDistance_AllOutfieldPlayers_BallNotInPossesion', pyxb.binding.datatypes.double)
    __avgDistance_AllOutfieldPlayers_BallNotInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 141, 15)
    __avgDistance_AllOutfieldPlayers_BallNotInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 141, 15)
    
    avgDistance_AllOutfieldPlayers_BallNotInPossesion = property(__avgDistance_AllOutfieldPlayers_BallNotInPossesion.value, __avgDistance_AllOutfieldPlayers_BallNotInPossesion.set, None, None)

    
    # Attribute avgDistance_Defenders uses Python identifier avgDistance_Defenders
    __avgDistance_Defenders = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_Defenders'), 'avgDistance_Defenders', '__AbsentNamespace0_CTD_ANON_15_avgDistance_Defenders', pyxb.binding.datatypes.double)
    __avgDistance_Defenders._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 142, 15)
    __avgDistance_Defenders._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 142, 15)
    
    avgDistance_Defenders = property(__avgDistance_Defenders.value, __avgDistance_Defenders.set, None, None)

    
    # Attribute avgDistance_Midfielders uses Python identifier avgDistance_Midfielders
    __avgDistance_Midfielders = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_Midfielders'), 'avgDistance_Midfielders', '__AbsentNamespace0_CTD_ANON_15_avgDistance_Midfielders', pyxb.binding.datatypes.double)
    __avgDistance_Midfielders._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 143, 15)
    __avgDistance_Midfielders._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 143, 15)
    
    avgDistance_Midfielders = property(__avgDistance_Midfielders.value, __avgDistance_Midfielders.set, None, None)

    
    # Attribute avgDistance_LastDefender_EndLine uses Python identifier avgDistance_LastDefender_EndLine
    __avgDistance_LastDefender_EndLine = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_LastDefender_EndLine'), 'avgDistance_LastDefender_EndLine', '__AbsentNamespace0_CTD_ANON_15_avgDistance_LastDefender_EndLine', pyxb.binding.datatypes.double)
    __avgDistance_LastDefender_EndLine._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 144, 15)
    __avgDistance_LastDefender_EndLine._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 144, 15)
    
    avgDistance_LastDefender_EndLine = property(__avgDistance_LastDefender_EndLine.value, __avgDistance_LastDefender_EndLine.set, None, None)

    
    # Attribute avgDistance_LastDefender_Goalkeeper uses Python identifier avgDistance_LastDefender_Goalkeeper
    __avgDistance_LastDefender_Goalkeeper = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_LastDefender_Goalkeeper'), 'avgDistance_LastDefender_Goalkeeper', '__AbsentNamespace0_CTD_ANON_15_avgDistance_LastDefender_Goalkeeper', pyxb.binding.datatypes.double)
    __avgDistance_LastDefender_Goalkeeper._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 145, 15)
    __avgDistance_LastDefender_Goalkeeper._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 145, 15)
    
    avgDistance_LastDefender_Goalkeeper = property(__avgDistance_LastDefender_Goalkeeper.value, __avgDistance_LastDefender_Goalkeeper.set, None, None)

    
    # Attribute avgDistance_CenterBacks_DefensiveMidfielder uses Python identifier avgDistance_CenterBacks_DefensiveMidfielder
    __avgDistance_CenterBacks_DefensiveMidfielder = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_CenterBacks_DefensiveMidfielder'), 'avgDistance_CenterBacks_DefensiveMidfielder', '__AbsentNamespace0_CTD_ANON_15_avgDistance_CenterBacks_DefensiveMidfielder', pyxb.binding.datatypes.double)
    __avgDistance_CenterBacks_DefensiveMidfielder._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 146, 15)
    __avgDistance_CenterBacks_DefensiveMidfielder._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 146, 15)
    
    avgDistance_CenterBacks_DefensiveMidfielder = property(__avgDistance_CenterBacks_DefensiveMidfielder.value, __avgDistance_CenterBacks_DefensiveMidfielder.set, None, None)

    
    # Attribute avgDistance_Midfielder_Forwards uses Python identifier avgDistance_Midfielder_Forwards
    __avgDistance_Midfielder_Forwards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_Midfielder_Forwards'), 'avgDistance_Midfielder_Forwards', '__AbsentNamespace0_CTD_ANON_15_avgDistance_Midfielder_Forwards', pyxb.binding.datatypes.double)
    __avgDistance_Midfielder_Forwards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 147, 15)
    __avgDistance_Midfielder_Forwards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 147, 15)
    
    avgDistance_Midfielder_Forwards = property(__avgDistance_Midfielder_Forwards.value, __avgDistance_Midfielder_Forwards.set, None, None)

    
    # Attribute avgNumberOfPlayers_BehindBall_BallNotInPossesion uses Python identifier avgNumberOfPlayers_BehindBall_BallNotInPossesion
    __avgNumberOfPlayers_BehindBall_BallNotInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgNumberOfPlayers_BehindBall_BallNotInPossesion'), 'avgNumberOfPlayers_BehindBall_BallNotInPossesion', '__AbsentNamespace0_CTD_ANON_15_avgNumberOfPlayers_BehindBall_BallNotInPossesion', pyxb.binding.datatypes.double)
    __avgNumberOfPlayers_BehindBall_BallNotInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 148, 15)
    __avgNumberOfPlayers_BehindBall_BallNotInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 148, 15)
    
    avgNumberOfPlayers_BehindBall_BallNotInPossesion = property(__avgNumberOfPlayers_BehindBall_BallNotInPossesion.value, __avgNumberOfPlayers_BehindBall_BallNotInPossesion.set, None, None)

    
    # Attribute avgDistance_InFrontOfBall_BallInPossesion uses Python identifier avgDistance_InFrontOfBall_BallInPossesion
    __avgDistance_InFrontOfBall_BallInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_InFrontOfBall_BallInPossesion'), 'avgDistance_InFrontOfBall_BallInPossesion', '__AbsentNamespace0_CTD_ANON_15_avgDistance_InFrontOfBall_BallInPossesion', pyxb.binding.datatypes.double)
    __avgDistance_InFrontOfBall_BallInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 149, 15)
    __avgDistance_InFrontOfBall_BallInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 149, 15)
    
    avgDistance_InFrontOfBall_BallInPossesion = property(__avgDistance_InFrontOfBall_BallInPossesion.value, __avgDistance_InFrontOfBall_BallInPossesion.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __avgDistance_AllOutfieldPlayers.name() : __avgDistance_AllOutfieldPlayers,
        __avgDistance_AllOutfieldPlayers_BallInPossesion.name() : __avgDistance_AllOutfieldPlayers_BallInPossesion,
        __avgDistance_AllOutfieldPlayers_BallNotInPossesion.name() : __avgDistance_AllOutfieldPlayers_BallNotInPossesion,
        __avgDistance_Defenders.name() : __avgDistance_Defenders,
        __avgDistance_Midfielders.name() : __avgDistance_Midfielders,
        __avgDistance_LastDefender_EndLine.name() : __avgDistance_LastDefender_EndLine,
        __avgDistance_LastDefender_Goalkeeper.name() : __avgDistance_LastDefender_Goalkeeper,
        __avgDistance_CenterBacks_DefensiveMidfielder.name() : __avgDistance_CenterBacks_DefensiveMidfielder,
        __avgDistance_Midfielder_Forwards.name() : __avgDistance_Midfielder_Forwards,
        __avgNumberOfPlayers_BehindBall_BallNotInPossesion.name() : __avgNumberOfPlayers_BehindBall_BallNotInPossesion,
        __avgDistance_InFrontOfBall_BallInPossesion.name() : __avgDistance_InFrontOfBall_BallInPossesion
    })



sports_content = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sports-content'), CTD_ANON, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', sports_content.name().localName(), sports_content)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-metadata'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 8, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-event'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 20, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 8, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-event')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 20, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-title'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 11, 7)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-title')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 11, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'event-metadata'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 23, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team'), CTD_ANON_4, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 34, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'event-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 23, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'team')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 34, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team-metadata'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 37, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team-stats'), CTD_ANON_7, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 53, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team-stats-tracking'), CTD_ANON_12, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 115, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'team-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 37, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'team-stats')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 53, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'team-stats-tracking')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 115, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_3()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 40, 13)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 40, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_4()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team-stats-soccer'), CTD_ANON_8, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 56, 13)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'team-stats-soccer')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 56, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_5()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-soccer-offensive'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 59, 16)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-soccer-defensive'), CTD_ANON_10, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 78, 16)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-soccer-foul'), CTD_ANON_11, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 83, 16)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-soccer-offensive')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 59, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-soccer-defensive')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 78, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-soccer-foul')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 83, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_6()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-time'), CTD_ANON_13, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 118, 13)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-ball'), CTD_ANON_14, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 123, 13)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-position'), CTD_ANON_15, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 137, 13)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-time')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 118, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-ball')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 123, 13))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-position')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/team-stats.xsd', 137, 13))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_7()

