# ./player_stats1.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-12-30 11:41:31.141506 by PyXB version 1.2.4 using Python 2.7.6.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6a98d5a0-9010-11e4-8338-002710dca3dc')

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
    """Copyright (c) 2003 - 2011 proFILE Computersysteme GmbH.
    All Rights Reserved.
    proFILE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE SUITABILITY OF
    THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
    IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE,
    OR NON-INFRINGEMENT. proFILE SHALL NOT BE LIABLE FOR ANY DAMAGES SUFFERED
    BY LICENSEE AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE
    OR ITS DERIVATIVES."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 13, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sports-metadata uses Python identifier sports_metadata
    __sports_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-metadata'), 'sports_metadata', '__AbsentNamespace0_CTD_ANON_sports_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 15, 4), )

    
    sports_metadata = property(__sports_metadata.value, __sports_metadata.set, None, None)

    
    # Element sports-event uses Python identifier sports_event
    __sports_event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-event'), 'sports_event', '__AbsentNamespace0_CTD_ANON_sports_event', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 27, 4), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 16, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sports-title uses Python identifier sports_title
    __sports_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-title'), 'sports_title', '__AbsentNamespace0_CTD_ANON__sports_title', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 18, 7), )

    
    sports_title = property(__sports_title.value, __sports_title.set, None, None)

    
    # Attribute date-time uses Python identifier date_time
    __date_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-time'), 'date_time', '__AbsentNamespace0_CTD_ANON__date_time', pyxb.binding.datatypes.string)
    __date_time._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 20, 6)
    __date_time._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 20, 6)
    
    date_time = property(__date_time.value, __date_time.set, None, None)

    
    # Attribute doc-id uses Python identifier doc_id
    __doc_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'doc-id'), 'doc_id', '__AbsentNamespace0_CTD_ANON__doc_id', pyxb.binding.datatypes.string)
    __doc_id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 21, 6)
    __doc_id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 21, 6)
    
    doc_id = property(__doc_id.value, __doc_id.set, None, None)

    
    # Attribute publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publisher'), 'publisher', '__AbsentNamespace0_CTD_ANON__publisher', pyxb.binding.datatypes.string)
    __publisher._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 22, 6)
    __publisher._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 22, 6)
    
    publisher = property(__publisher.value, __publisher.set, None, None)

    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'language'), 'language', '__AbsentNamespace0_CTD_ANON__language', pyxb.binding.datatypes.string)
    __language._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 23, 6)
    __language._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 23, 6)
    
    language = property(__language.value, __language.set, None, None)

    
    # Attribute document-class uses Python identifier document_class
    __document_class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'document-class'), 'document_class', '__AbsentNamespace0_CTD_ANON__document_class', pyxb.binding.datatypes.string)
    __document_class._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 24, 6)
    __document_class._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 24, 6)
    
    document_class = property(__document_class.value, __document_class.set, None, None)

    _ElementMap.update({
        __sports_title.name() : __sports_title
    })
    _AttributeMap.update({
        __date_time.name() : __date_time,
        __doc_id.name() : __doc_id,
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
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 28, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element event-metadata uses Python identifier event_metadata
    __event_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'event-metadata'), 'event_metadata', '__AbsentNamespace0_CTD_ANON_2_event_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 30, 7), )

    
    event_metadata = property(__event_metadata.value, __event_metadata.set, None, None)

    
    # Element team uses Python identifier team
    __team = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team'), 'team', '__AbsentNamespace0_CTD_ANON_2_team', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 45, 7), )

    
    team = property(__team.value, __team.set, None, None)

    _ElementMap.update({
        __event_metadata.name() : __event_metadata,
        __team.name() : __team
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 31, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_3_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 34, 11)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 34, 11)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute event-key uses Python identifier event_key
    __event_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'event-key'), 'event_key', '__AbsentNamespace0_CTD_ANON_3_event_key', pyxb.binding.datatypes.int)
    __event_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 35, 11)
    __event_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 35, 11)
    
    event_key = property(__event_key.value, __event_key.set, None, None)

    
    # Attribute event-status uses Python identifier event_status
    __event_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'event-status'), 'event_status', '__AbsentNamespace0_CTD_ANON_3_event_status', pyxb.binding.datatypes.string)
    __event_status._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 36, 11)
    __event_status._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 36, 11)
    
    event_status = property(__event_status.value, __event_status.set, None, None)

    
    # Attribute start-date-time uses Python identifier start_date_time
    __start_date_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-date-time'), 'start_date_time', '__AbsentNamespace0_CTD_ANON_3_start_date_time', pyxb.binding.datatypes.string)
    __start_date_time._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 37, 11)
    __start_date_time._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 37, 11)
    
    start_date_time = property(__start_date_time.value, __start_date_time.set, None, None)

    
    # Attribute start-weekday uses Python identifier start_weekday
    __start_weekday = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-weekday'), 'start_weekday', '__AbsentNamespace0_CTD_ANON_3_start_weekday', pyxb.binding.datatypes.string)
    __start_weekday._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 38, 11)
    __start_weekday._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 38, 11)
    
    start_weekday = property(__start_weekday.value, __start_weekday.set, None, None)

    
    # Attribute heat-number uses Python identifier heat_number
    __heat_number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'heat-number'), 'heat_number', '__AbsentNamespace0_CTD_ANON_3_heat_number', pyxb.binding.datatypes.byte)
    __heat_number._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 39, 11)
    __heat_number._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 39, 11)
    
    heat_number = property(__heat_number.value, __heat_number.set, None, None)

    
    # Attribute site-attendance uses Python identifier site_attendance
    __site_attendance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'site-attendance'), 'site_attendance', '__AbsentNamespace0_CTD_ANON_3_site_attendance', pyxb.binding.datatypes.int)
    __site_attendance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 40, 11)
    __site_attendance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 40, 11)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 46, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element team-metadata uses Python identifier team_metadata
    __team_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team-metadata'), 'team_metadata', '__AbsentNamespace0_CTD_ANON_4_team_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 48, 10), )

    
    team_metadata = property(__team_metadata.value, __team_metadata.set, None, None)

    
    # Element player uses Python identifier player
    __player = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'player'), 'player', '__AbsentNamespace0_CTD_ANON_4_player', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 66, 10), )

    
    player = property(__player.value, __player.set, None, None)

    _ElementMap.update({
        __team_metadata.name() : __team_metadata,
        __player.name() : __player
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
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 49, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_5_name', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 51, 13), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_5_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 62, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 62, 12)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute team-key uses Python identifier team_key
    __team_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'team-key'), 'team_key', '__AbsentNamespace0_CTD_ANON_5_team_key', pyxb.binding.datatypes.byte)
    __team_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 63, 12)
    __team_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 63, 12)
    
    team_key = property(__team_key.value, __team_key.set, None, None)

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __id.name() : __id,
        __team_key.name() : __team_key
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 52, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__AbsentNamespace0_CTD_ANON_6_full', pyxb.binding.datatypes.string)
    __full._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 55, 17)
    __full._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 55, 17)
    
    full = property(__full.value, __full.set, None, None)

    
    # Attribute nickname uses Python identifier nickname
    __nickname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nickname'), 'nickname', '__AbsentNamespace0_CTD_ANON_6_nickname', pyxb.binding.datatypes.string)
    __nickname._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 56, 17)
    __nickname._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 56, 17)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 67, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element player-metadata uses Python identifier player_metadata
    __player_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'player-metadata'), 'player_metadata', '__AbsentNamespace0_CTD_ANON_7_player_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 69, 13), )

    
    player_metadata = property(__player_metadata.value, __player_metadata.set, None, None)

    
    # Element player-stats uses Python identifier player_stats
    __player_stats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'player-stats'), 'player_stats', '__AbsentNamespace0_CTD_ANON_7_player_stats', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 90, 13), )

    
    player_stats = property(__player_stats.value, __player_stats.set, None, None)

    _ElementMap.update({
        __player_metadata.name() : __player_metadata,
        __player_stats.name() : __player_stats
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 70, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_8_name', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 72, 16), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute player-key uses Python identifier player_key
    __player_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-key'), 'player_key', '__AbsentNamespace0_CTD_ANON_8_player_key', pyxb.binding.datatypes.int)
    __player_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 86, 15)
    __player_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 86, 15)
    
    player_key = property(__player_key.value, __player_key.set, None, None)

    
    # Attribute uniform-number uses Python identifier uniform_number
    __uniform_number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uniform-number'), 'uniform_number', '__AbsentNamespace0_CTD_ANON_8_uniform_number', pyxb.binding.datatypes.byte)
    __uniform_number._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 87, 15)
    __uniform_number._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 87, 15)
    
    uniform_number = property(__uniform_number.value, __uniform_number.set, None, None)

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __player_key.name() : __player_key,
        __uniform_number.name() : __uniform_number
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 73, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute first uses Python identifier first
    __first = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'first'), 'first', '__AbsentNamespace0_CTD_ANON_9_first', pyxb.binding.datatypes.string)
    __first._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 76, 20)
    __first._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 76, 20)
    
    first = property(__first.value, __first.set, None, None)

    
    # Attribute last uses Python identifier last
    __last = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'last'), 'last', '__AbsentNamespace0_CTD_ANON_9_last', pyxb.binding.datatypes.string)
    __last._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 77, 20)
    __last._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 77, 20)
    
    last = property(__last.value, __last.set, None, None)

    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__AbsentNamespace0_CTD_ANON_9_full', pyxb.binding.datatypes.string)
    __full._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 78, 20)
    __full._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 78, 20)
    
    full = property(__full.value, __full.set, None, None)

    
    # Attribute nickname uses Python identifier nickname
    __nickname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nickname'), 'nickname', '__AbsentNamespace0_CTD_ANON_9_nickname', pyxb.binding.datatypes.string)
    __nickname._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 79, 20)
    __nickname._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 79, 20)
    
    nickname = property(__nickname.value, __nickname.set, None, None)

    
    # Attribute extensive uses Python identifier extensive
    __extensive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'extensive'), 'extensive', '__AbsentNamespace0_CTD_ANON_9_extensive', pyxb.binding.datatypes.string)
    __extensive._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 80, 20)
    __extensive._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 80, 20)
    
    extensive = property(__extensive.value, __extensive.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __first.name() : __first,
        __last.name() : __last,
        __full.name() : __full,
        __nickname.name() : __nickname,
        __extensive.name() : __extensive
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 91, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element rating uses Python identifier rating
    __rating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rating'), 'rating', '__AbsentNamespace0_CTD_ANON_10_rating', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 93, 16), )

    
    rating = property(__rating.value, __rating.set, None, None)

    
    # Element player-stats-soccer uses Python identifier player_stats_soccer
    __player_stats_soccer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'player-stats-soccer'), 'player_stats_soccer', '__AbsentNamespace0_CTD_ANON_10_player_stats_soccer', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 107, 16), )

    
    player_stats_soccer = property(__player_stats_soccer.value, __player_stats_soccer.set, None, None)

    
    # Element player-stats-tracking uses Python identifier player_stats_tracking
    __player_stats_tracking = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'player-stats-tracking'), 'player_stats_tracking', '__AbsentNamespace0_CTD_ANON_10_player_stats_tracking', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 185, 16), )

    
    player_stats_tracking = property(__player_stats_tracking.value, __player_stats_tracking.set, None, None)

    
    # Attribute stats-coverage uses Python identifier stats_coverage
    __stats_coverage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stats-coverage'), 'stats_coverage', '__AbsentNamespace0_CTD_ANON_10_stats_coverage', pyxb.binding.datatypes.string)
    __stats_coverage._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 320, 15)
    __stats_coverage._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 320, 15)
    
    stats_coverage = property(__stats_coverage.value, __stats_coverage.set, None, None)

    
    # Attribute date-coverage-type uses Python identifier date_coverage_type
    __date_coverage_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-coverage-type'), 'date_coverage_type', '__AbsentNamespace0_CTD_ANON_10_date_coverage_type', pyxb.binding.datatypes.string)
    __date_coverage_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 321, 15)
    __date_coverage_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 321, 15)
    
    date_coverage_type = property(__date_coverage_type.value, __date_coverage_type.set, None, None)

    
    # Attribute score uses Python identifier score
    __score = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score'), 'score', '__AbsentNamespace0_CTD_ANON_10_score', pyxb.binding.datatypes.byte)
    __score._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 322, 15)
    __score._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 322, 15)
    
    score = property(__score.value, __score.set, None, None)

    _ElementMap.update({
        __rating.name() : __rating,
        __player_stats_soccer.name() : __player_stats_soccer,
        __player_stats_tracking.name() : __player_stats_tracking
    })
    _AttributeMap.update({
        __stats_coverage.name() : __stats_coverage,
        __date_coverage_type.name() : __date_coverage_type,
        __score.name() : __score
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 94, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute rating-type uses Python identifier rating_type
    __rating_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rating-type'), 'rating_type', '__AbsentNamespace0_CTD_ANON_11_rating_type', pyxb.binding.datatypes.string)
    __rating_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 97, 20)
    __rating_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 97, 20)
    
    rating_type = property(__rating_type.value, __rating_type.set, None, None)

    
    # Attribute rating-value-goalie uses Python identifier rating_value_goalie
    __rating_value_goalie = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rating-value-goalie'), 'rating_value_goalie', '__AbsentNamespace0_CTD_ANON_11_rating_value_goalie', pyxb.binding.datatypes.string)
    __rating_value_goalie._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 98, 20)
    __rating_value_goalie._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 98, 20)
    
    rating_value_goalie = property(__rating_value_goalie.value, __rating_value_goalie.set, None, None)

    
    # Attribute rating-value-defenseman uses Python identifier rating_value_defenseman
    __rating_value_defenseman = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rating-value-defenseman'), 'rating_value_defenseman', '__AbsentNamespace0_CTD_ANON_11_rating_value_defenseman', pyxb.binding.datatypes.string)
    __rating_value_defenseman._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 99, 20)
    __rating_value_defenseman._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 99, 20)
    
    rating_value_defenseman = property(__rating_value_defenseman.value, __rating_value_defenseman.set, None, None)

    
    # Attribute rating-value-mid-fielder uses Python identifier rating_value_mid_fielder
    __rating_value_mid_fielder = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rating-value-mid-fielder'), 'rating_value_mid_fielder', '__AbsentNamespace0_CTD_ANON_11_rating_value_mid_fielder', pyxb.binding.datatypes.string)
    __rating_value_mid_fielder._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 100, 20)
    __rating_value_mid_fielder._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 100, 20)
    
    rating_value_mid_fielder = property(__rating_value_mid_fielder.value, __rating_value_mid_fielder.set, None, None)

    
    # Attribute rating-value-forward uses Python identifier rating_value_forward
    __rating_value_forward = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rating-value-forward'), 'rating_value_forward', '__AbsentNamespace0_CTD_ANON_11_rating_value_forward', pyxb.binding.datatypes.string)
    __rating_value_forward._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 101, 20)
    __rating_value_forward._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 101, 20)
    
    rating_value_forward = property(__rating_value_forward.value, __rating_value_forward.set, None, None)

    
    # Attribute rating-value uses Python identifier rating_value
    __rating_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rating-value'), 'rating_value', '__AbsentNamespace0_CTD_ANON_11_rating_value', pyxb.binding.datatypes.string)
    __rating_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 102, 20)
    __rating_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 102, 20)
    
    rating_value = property(__rating_value.value, __rating_value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rating_type.name() : __rating_type,
        __rating_value_goalie.name() : __rating_value_goalie,
        __rating_value_defenseman.name() : __rating_value_defenseman,
        __rating_value_mid_fielder.name() : __rating_value_mid_fielder,
        __rating_value_forward.name() : __rating_value_forward,
        __rating_value.name() : __rating_value
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 108, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element stats-soccer-defensive uses Python identifier stats_soccer_defensive
    __stats_soccer_defensive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-soccer-defensive'), 'stats_soccer_defensive', '__AbsentNamespace0_CTD_ANON_12_stats_soccer_defensive', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 110, 19), )

    
    stats_soccer_defensive = property(__stats_soccer_defensive.value, __stats_soccer_defensive.set, None, None)

    
    # Element stats-soccer-offensive uses Python identifier stats_soccer_offensive
    __stats_soccer_offensive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-soccer-offensive'), 'stats_soccer_offensive', '__AbsentNamespace0_CTD_ANON_12_stats_soccer_offensive', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 123, 19), )

    
    stats_soccer_offensive = property(__stats_soccer_offensive.value, __stats_soccer_offensive.set, None, None)

    
    # Element stats-soccer-foul uses Python identifier stats_soccer_foul
    __stats_soccer_foul = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-soccer-foul'), 'stats_soccer_foul', '__AbsentNamespace0_CTD_ANON_12_stats_soccer_foul', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 149, 19), )

    
    stats_soccer_foul = property(__stats_soccer_foul.value, __stats_soccer_foul.set, None, None)

    
    # Attribute duels-won uses Python identifier duels_won
    __duels_won = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-won'), 'duels_won', '__AbsentNamespace0_CTD_ANON_12_duels_won', pyxb.binding.datatypes.byte)
    __duels_won._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 163, 18)
    __duels_won._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 163, 18)
    
    duels_won = property(__duels_won.value, __duels_won.set, None, None)

    
    # Attribute duels-won-ground uses Python identifier duels_won_ground
    __duels_won_ground = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-won-ground'), 'duels_won_ground', '__AbsentNamespace0_CTD_ANON_12_duels_won_ground', pyxb.binding.datatypes.byte)
    __duels_won_ground._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 164, 18)
    __duels_won_ground._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 164, 18)
    
    duels_won_ground = property(__duels_won_ground.value, __duels_won_ground.set, None, None)

    
    # Attribute duels-won-header uses Python identifier duels_won_header
    __duels_won_header = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-won-header'), 'duels_won_header', '__AbsentNamespace0_CTD_ANON_12_duels_won_header', pyxb.binding.datatypes.byte)
    __duels_won_header._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 165, 18)
    __duels_won_header._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 165, 18)
    
    duels_won_header = property(__duels_won_header.value, __duels_won_header.set, None, None)

    
    # Attribute duels-lost uses Python identifier duels_lost
    __duels_lost = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-lost'), 'duels_lost', '__AbsentNamespace0_CTD_ANON_12_duels_lost', pyxb.binding.datatypes.byte)
    __duels_lost._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 166, 18)
    __duels_lost._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 166, 18)
    
    duels_lost = property(__duels_lost.value, __duels_lost.set, None, None)

    
    # Attribute duels-lost-ground uses Python identifier duels_lost_ground
    __duels_lost_ground = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-lost-ground'), 'duels_lost_ground', '__AbsentNamespace0_CTD_ANON_12_duels_lost_ground', pyxb.binding.datatypes.byte)
    __duels_lost_ground._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 167, 18)
    __duels_lost_ground._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 167, 18)
    
    duels_lost_ground = property(__duels_lost_ground.value, __duels_lost_ground.set, None, None)

    
    # Attribute duels-lost-header uses Python identifier duels_lost_header
    __duels_lost_header = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-lost-header'), 'duels_lost_header', '__AbsentNamespace0_CTD_ANON_12_duels_lost_header', pyxb.binding.datatypes.byte)
    __duels_lost_header._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 168, 18)
    __duels_lost_header._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 168, 18)
    
    duels_lost_header = property(__duels_lost_header.value, __duels_lost_header.set, None, None)

    
    # Attribute duels-won-percentage uses Python identifier duels_won_percentage
    __duels_won_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels-won-percentage'), 'duels_won_percentage', '__AbsentNamespace0_CTD_ANON_12_duels_won_percentage', pyxb.binding.datatypes.float)
    __duels_won_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 169, 18)
    __duels_won_percentage._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 169, 18)
    
    duels_won_percentage = property(__duels_won_percentage.value, __duels_won_percentage.set, None, None)

    
    # Attribute passes-completed uses Python identifier passes_completed
    __passes_completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes-completed'), 'passes_completed', '__AbsentNamespace0_CTD_ANON_12_passes_completed', pyxb.binding.datatypes.byte)
    __passes_completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 170, 18)
    __passes_completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 170, 18)
    
    passes_completed = property(__passes_completed.value, __passes_completed.set, None, None)

    
    # Attribute passes-failed uses Python identifier passes_failed
    __passes_failed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes-failed'), 'passes_failed', '__AbsentNamespace0_CTD_ANON_12_passes_failed', pyxb.binding.datatypes.byte)
    __passes_failed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 171, 18)
    __passes_failed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 171, 18)
    
    passes_failed = property(__passes_failed.value, __passes_failed.set, None, None)

    
    # Attribute passes-completions-percentage uses Python identifier passes_completions_percentage
    __passes_completions_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes-completions-percentage'), 'passes_completions_percentage', '__AbsentNamespace0_CTD_ANON_12_passes_completions_percentage', pyxb.binding.datatypes.float)
    __passes_completions_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 172, 18)
    __passes_completions_percentage._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 172, 18)
    
    passes_completions_percentage = property(__passes_completions_percentage.value, __passes_completions_percentage.set, None, None)

    
    # Attribute passes-failed-percentage uses Python identifier passes_failed_percentage
    __passes_failed_percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes-failed-percentage'), 'passes_failed_percentage', '__AbsentNamespace0_CTD_ANON_12_passes_failed_percentage', pyxb.binding.datatypes.float)
    __passes_failed_percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 173, 18)
    __passes_failed_percentage._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 173, 18)
    
    passes_failed_percentage = property(__passes_failed_percentage.value, __passes_failed_percentage.set, None, None)

    
    # Attribute passes uses Python identifier passes
    __passes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes'), 'passes', '__AbsentNamespace0_CTD_ANON_12_passes', pyxb.binding.datatypes.byte)
    __passes._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 174, 18)
    __passes._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 174, 18)
    
    passes = property(__passes.value, __passes.set, None, None)

    
    # Attribute balls-touched uses Python identifier balls_touched
    __balls_touched = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'balls-touched'), 'balls_touched', '__AbsentNamespace0_CTD_ANON_12_balls_touched', pyxb.binding.datatypes.byte)
    __balls_touched._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 175, 18)
    __balls_touched._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 175, 18)
    
    balls_touched = property(__balls_touched.value, __balls_touched.set, None, None)

    
    # Attribute tracking-distance uses Python identifier tracking_distance
    __tracking_distance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-distance'), 'tracking_distance', '__AbsentNamespace0_CTD_ANON_12_tracking_distance', pyxb.binding.datatypes.float)
    __tracking_distance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 176, 18)
    __tracking_distance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 176, 18)
    
    tracking_distance = property(__tracking_distance.value, __tracking_distance.set, None, None)

    
    # Attribute tracking-average-speed uses Python identifier tracking_average_speed
    __tracking_average_speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-average-speed'), 'tracking_average_speed', '__AbsentNamespace0_CTD_ANON_12_tracking_average_speed', pyxb.binding.datatypes.float)
    __tracking_average_speed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 177, 18)
    __tracking_average_speed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 177, 18)
    
    tracking_average_speed = property(__tracking_average_speed.value, __tracking_average_speed.set, None, None)

    
    # Attribute tracking-max-speed uses Python identifier tracking_max_speed
    __tracking_max_speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-max-speed'), 'tracking_max_speed', '__AbsentNamespace0_CTD_ANON_12_tracking_max_speed', pyxb.binding.datatypes.float)
    __tracking_max_speed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 178, 18)
    __tracking_max_speed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 178, 18)
    
    tracking_max_speed = property(__tracking_max_speed.value, __tracking_max_speed.set, None, None)

    
    # Attribute tracking-sprints uses Python identifier tracking_sprints
    __tracking_sprints = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-sprints'), 'tracking_sprints', '__AbsentNamespace0_CTD_ANON_12_tracking_sprints', pyxb.binding.datatypes.byte)
    __tracking_sprints._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 179, 18)
    __tracking_sprints._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 179, 18)
    
    tracking_sprints = property(__tracking_sprints.value, __tracking_sprints.set, None, None)

    
    # Attribute tracking-sprints-distance uses Python identifier tracking_sprints_distance
    __tracking_sprints_distance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-sprints-distance'), 'tracking_sprints_distance', '__AbsentNamespace0_CTD_ANON_12_tracking_sprints_distance', pyxb.binding.datatypes.float)
    __tracking_sprints_distance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 180, 18)
    __tracking_sprints_distance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 180, 18)
    
    tracking_sprints_distance = property(__tracking_sprints_distance.value, __tracking_sprints_distance.set, None, None)

    
    # Attribute tracking-fast-runs uses Python identifier tracking_fast_runs
    __tracking_fast_runs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-fast-runs'), 'tracking_fast_runs', '__AbsentNamespace0_CTD_ANON_12_tracking_fast_runs', pyxb.binding.datatypes.byte)
    __tracking_fast_runs._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 181, 18)
    __tracking_fast_runs._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 181, 18)
    
    tracking_fast_runs = property(__tracking_fast_runs.value, __tracking_fast_runs.set, None, None)

    
    # Attribute tracking-fast-runs-distance uses Python identifier tracking_fast_runs_distance
    __tracking_fast_runs_distance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tracking-fast-runs-distance'), 'tracking_fast_runs_distance', '__AbsentNamespace0_CTD_ANON_12_tracking_fast_runs_distance', pyxb.binding.datatypes.float)
    __tracking_fast_runs_distance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 182, 18)
    __tracking_fast_runs_distance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 182, 18)
    
    tracking_fast_runs_distance = property(__tracking_fast_runs_distance.value, __tracking_fast_runs_distance.set, None, None)

    _ElementMap.update({
        __stats_soccer_defensive.name() : __stats_soccer_defensive,
        __stats_soccer_offensive.name() : __stats_soccer_offensive,
        __stats_soccer_foul.name() : __stats_soccer_foul
    })
    _AttributeMap.update({
        __duels_won.name() : __duels_won,
        __duels_won_ground.name() : __duels_won_ground,
        __duels_won_header.name() : __duels_won_header,
        __duels_lost.name() : __duels_lost,
        __duels_lost_ground.name() : __duels_lost_ground,
        __duels_lost_header.name() : __duels_lost_header,
        __duels_won_percentage.name() : __duels_won_percentage,
        __passes_completed.name() : __passes_completed,
        __passes_failed.name() : __passes_failed,
        __passes_completions_percentage.name() : __passes_completions_percentage,
        __passes_failed_percentage.name() : __passes_failed_percentage,
        __passes.name() : __passes,
        __balls_touched.name() : __balls_touched,
        __tracking_distance.name() : __tracking_distance,
        __tracking_average_speed.name() : __tracking_average_speed,
        __tracking_max_speed.name() : __tracking_max_speed,
        __tracking_sprints.name() : __tracking_sprints,
        __tracking_sprints_distance.name() : __tracking_sprints_distance,
        __tracking_fast_runs.name() : __tracking_fast_runs,
        __tracking_fast_runs_distance.name() : __tracking_fast_runs_distance
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 111, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute saves uses Python identifier saves
    __saves = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'saves'), 'saves', '__AbsentNamespace0_CTD_ANON_13_saves', pyxb.binding.datatypes.byte)
    __saves._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 114, 23)
    __saves._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 114, 23)
    
    saves = property(__saves.value, __saves.set, None, None)

    
    # Attribute catches-punches-crosses uses Python identifier catches_punches_crosses
    __catches_punches_crosses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'catches-punches-crosses'), 'catches_punches_crosses', '__AbsentNamespace0_CTD_ANON_13_catches_punches_crosses', pyxb.binding.datatypes.byte)
    __catches_punches_crosses._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 115, 23)
    __catches_punches_crosses._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 115, 23)
    
    catches_punches_crosses = property(__catches_punches_crosses.value, __catches_punches_crosses.set, None, None)

    
    # Attribute catches-punches-corners uses Python identifier catches_punches_corners
    __catches_punches_corners = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'catches-punches-corners'), 'catches_punches_corners', '__AbsentNamespace0_CTD_ANON_13_catches_punches_corners', pyxb.binding.datatypes.byte)
    __catches_punches_corners._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 116, 23)
    __catches_punches_corners._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 116, 23)
    
    catches_punches_corners = property(__catches_punches_corners.value, __catches_punches_corners.set, None, None)

    
    # Attribute goals-against-total uses Python identifier goals_against_total
    __goals_against_total = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'goals-against-total'), 'goals_against_total', '__AbsentNamespace0_CTD_ANON_13_goals_against_total', pyxb.binding.datatypes.byte)
    __goals_against_total._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 117, 23)
    __goals_against_total._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 117, 23)
    
    goals_against_total = property(__goals_against_total.value, __goals_against_total.set, None, None)

    
    # Attribute penalty-saves uses Python identifier penalty_saves
    __penalty_saves = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'penalty-saves'), 'penalty_saves', '__AbsentNamespace0_CTD_ANON_13_penalty_saves', pyxb.binding.datatypes.byte)
    __penalty_saves._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 118, 23)
    __penalty_saves._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 118, 23)
    
    penalty_saves = property(__penalty_saves.value, __penalty_saves.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __saves.name() : __saves,
        __catches_punches_crosses.name() : __catches_punches_crosses,
        __catches_punches_corners.name() : __catches_punches_corners,
        __goals_against_total.name() : __goals_against_total,
        __penalty_saves.name() : __penalty_saves
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 124, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute shots-total uses Python identifier shots_total
    __shots_total = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-total'), 'shots_total', '__AbsentNamespace0_CTD_ANON_14_shots_total', pyxb.binding.datatypes.byte)
    __shots_total._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 127, 23)
    __shots_total._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 127, 23)
    
    shots_total = property(__shots_total.value, __shots_total.set, None, None)

    
    # Attribute offsides uses Python identifier offsides
    __offsides = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offsides'), 'offsides', '__AbsentNamespace0_CTD_ANON_14_offsides', pyxb.binding.datatypes.byte)
    __offsides._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 128, 23)
    __offsides._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 128, 23)
    
    offsides = property(__offsides.value, __offsides.set, None, None)

    
    # Attribute corner-kicks uses Python identifier corner_kicks
    __corner_kicks = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'corner-kicks'), 'corner_kicks', '__AbsentNamespace0_CTD_ANON_14_corner_kicks', pyxb.binding.datatypes.byte)
    __corner_kicks._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 129, 23)
    __corner_kicks._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 129, 23)
    
    corner_kicks = property(__corner_kicks.value, __corner_kicks.set, None, None)

    
    # Attribute crosses uses Python identifier crosses
    __crosses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crosses'), 'crosses', '__AbsentNamespace0_CTD_ANON_14_crosses', pyxb.binding.datatypes.byte)
    __crosses._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 130, 23)
    __crosses._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 130, 23)
    
    crosses = property(__crosses.value, __crosses.set, None, None)

    
    # Attribute assists-total uses Python identifier assists_total
    __assists_total = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'assists-total'), 'assists_total', '__AbsentNamespace0_CTD_ANON_14_assists_total', pyxb.binding.datatypes.byte)
    __assists_total._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 131, 23)
    __assists_total._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 131, 23)
    
    assists_total = property(__assists_total.value, __assists_total.set, None, None)

    
    # Attribute shot-assists uses Python identifier shot_assists
    __shot_assists = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shot-assists'), 'shot_assists', '__AbsentNamespace0_CTD_ANON_14_shot_assists', pyxb.binding.datatypes.byte)
    __shot_assists._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 132, 23)
    __shot_assists._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 132, 23)
    
    shot_assists = property(__shot_assists.value, __shot_assists.set, None, None)

    
    # Attribute freekicks uses Python identifier freekicks
    __freekicks = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'freekicks'), 'freekicks', '__AbsentNamespace0_CTD_ANON_14_freekicks', pyxb.binding.datatypes.byte)
    __freekicks._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 133, 23)
    __freekicks._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 133, 23)
    
    freekicks = property(__freekicks.value, __freekicks.set, None, None)

    
    # Attribute miss-chance uses Python identifier miss_chance
    __miss_chance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'miss-chance'), 'miss_chance', '__AbsentNamespace0_CTD_ANON_14_miss_chance', pyxb.binding.datatypes.byte)
    __miss_chance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 134, 23)
    __miss_chance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 134, 23)
    
    miss_chance = property(__miss_chance.value, __miss_chance.set, None, None)

    
    # Attribute throw-in uses Python identifier throw_in
    __throw_in = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'throw-in'), 'throw_in', '__AbsentNamespace0_CTD_ANON_14_throw_in', pyxb.binding.datatypes.byte)
    __throw_in._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 135, 23)
    __throw_in._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 135, 23)
    
    throw_in = property(__throw_in.value, __throw_in.set, None, None)

    
    # Attribute punt uses Python identifier punt
    __punt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'punt'), 'punt', '__AbsentNamespace0_CTD_ANON_14_punt', pyxb.binding.datatypes.byte)
    __punt._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 136, 23)
    __punt._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 136, 23)
    
    punt = property(__punt.value, __punt.set, None, None)

    
    # Attribute shots-penalty-shot-scored uses Python identifier shots_penalty_shot_scored
    __shots_penalty_shot_scored = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-penalty-shot-scored'), 'shots_penalty_shot_scored', '__AbsentNamespace0_CTD_ANON_14_shots_penalty_shot_scored', pyxb.binding.datatypes.byte)
    __shots_penalty_shot_scored._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 137, 23)
    __shots_penalty_shot_scored._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 137, 23)
    
    shots_penalty_shot_scored = property(__shots_penalty_shot_scored.value, __shots_penalty_shot_scored.set, None, None)

    
    # Attribute shots-penalty-shot-missed uses Python identifier shots_penalty_shot_missed
    __shots_penalty_shot_missed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-penalty-shot-missed'), 'shots_penalty_shot_missed', '__AbsentNamespace0_CTD_ANON_14_shots_penalty_shot_missed', pyxb.binding.datatypes.byte)
    __shots_penalty_shot_missed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 138, 23)
    __shots_penalty_shot_missed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 138, 23)
    
    shots_penalty_shot_missed = property(__shots_penalty_shot_missed.value, __shots_penalty_shot_missed.set, None, None)

    
    # Attribute dfl-assists-total uses Python identifier dfl_assists_total
    __dfl_assists_total = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dfl-assists-total'), 'dfl_assists_total', '__AbsentNamespace0_CTD_ANON_14_dfl_assists_total', pyxb.binding.datatypes.byte)
    __dfl_assists_total._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 139, 23)
    __dfl_assists_total._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 139, 23)
    
    dfl_assists_total = property(__dfl_assists_total.value, __dfl_assists_total.set, None, None)

    
    # Attribute shots-total-outside-box uses Python identifier shots_total_outside_box
    __shots_total_outside_box = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-total-outside-box'), 'shots_total_outside_box', '__AbsentNamespace0_CTD_ANON_14_shots_total_outside_box', pyxb.binding.datatypes.byte)
    __shots_total_outside_box._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 140, 23)
    __shots_total_outside_box._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 140, 23)
    
    shots_total_outside_box = property(__shots_total_outside_box.value, __shots_total_outside_box.set, None, None)

    
    # Attribute shots-total-inside-box uses Python identifier shots_total_inside_box
    __shots_total_inside_box = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-total-inside-box'), 'shots_total_inside_box', '__AbsentNamespace0_CTD_ANON_14_shots_total_inside_box', pyxb.binding.datatypes.byte)
    __shots_total_inside_box._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 141, 23)
    __shots_total_inside_box._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 141, 23)
    
    shots_total_inside_box = property(__shots_total_inside_box.value, __shots_total_inside_box.set, None, None)

    
    # Attribute shots-foot-inside-box uses Python identifier shots_foot_inside_box
    __shots_foot_inside_box = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-foot-inside-box'), 'shots_foot_inside_box', '__AbsentNamespace0_CTD_ANON_14_shots_foot_inside_box', pyxb.binding.datatypes.byte)
    __shots_foot_inside_box._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 142, 23)
    __shots_foot_inside_box._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 142, 23)
    
    shots_foot_inside_box = property(__shots_foot_inside_box.value, __shots_foot_inside_box.set, None, None)

    
    # Attribute shots-foot-outside-box uses Python identifier shots_foot_outside_box
    __shots_foot_outside_box = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-foot-outside-box'), 'shots_foot_outside_box', '__AbsentNamespace0_CTD_ANON_14_shots_foot_outside_box', pyxb.binding.datatypes.byte)
    __shots_foot_outside_box._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 143, 23)
    __shots_foot_outside_box._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 143, 23)
    
    shots_foot_outside_box = property(__shots_foot_outside_box.value, __shots_foot_outside_box.set, None, None)

    
    # Attribute shots-total-header uses Python identifier shots_total_header
    __shots_total_header = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shots-total-header'), 'shots_total_header', '__AbsentNamespace0_CTD_ANON_14_shots_total_header', pyxb.binding.datatypes.byte)
    __shots_total_header._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 144, 23)
    __shots_total_header._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 144, 23)
    
    shots_total_header = property(__shots_total_header.value, __shots_total_header.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __shots_total.name() : __shots_total,
        __offsides.name() : __offsides,
        __corner_kicks.name() : __corner_kicks,
        __crosses.name() : __crosses,
        __assists_total.name() : __assists_total,
        __shot_assists.name() : __shot_assists,
        __freekicks.name() : __freekicks,
        __miss_chance.name() : __miss_chance,
        __throw_in.name() : __throw_in,
        __punt.name() : __punt,
        __shots_penalty_shot_scored.name() : __shots_penalty_shot_scored,
        __shots_penalty_shot_missed.name() : __shots_penalty_shot_missed,
        __dfl_assists_total.name() : __dfl_assists_total,
        __shots_total_outside_box.name() : __shots_total_outside_box,
        __shots_total_inside_box.name() : __shots_total_inside_box,
        __shots_foot_inside_box.name() : __shots_foot_inside_box,
        __shots_foot_outside_box.name() : __shots_foot_outside_box,
        __shots_total_header.name() : __shots_total_header
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 150, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute fouls-commited uses Python identifier fouls_commited
    __fouls_commited = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fouls-commited'), 'fouls_commited', '__AbsentNamespace0_CTD_ANON_15_fouls_commited', pyxb.binding.datatypes.byte)
    __fouls_commited._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 153, 23)
    __fouls_commited._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 153, 23)
    
    fouls_commited = property(__fouls_commited.value, __fouls_commited.set, None, None)

    
    # Attribute fouls-suffered uses Python identifier fouls_suffered
    __fouls_suffered = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fouls-suffered'), 'fouls_suffered', '__AbsentNamespace0_CTD_ANON_15_fouls_suffered', pyxb.binding.datatypes.byte)
    __fouls_suffered._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 154, 23)
    __fouls_suffered._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 154, 23)
    
    fouls_suffered = property(__fouls_suffered.value, __fouls_suffered.set, None, None)

    
    # Attribute yellow-red-cards uses Python identifier yellow_red_cards
    __yellow_red_cards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'yellow-red-cards'), 'yellow_red_cards', '__AbsentNamespace0_CTD_ANON_15_yellow_red_cards', pyxb.binding.datatypes.byte)
    __yellow_red_cards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 155, 23)
    __yellow_red_cards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 155, 23)
    
    yellow_red_cards = property(__yellow_red_cards.value, __yellow_red_cards.set, None, None)

    
    # Attribute red-cards uses Python identifier red_cards
    __red_cards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'red-cards'), 'red_cards', '__AbsentNamespace0_CTD_ANON_15_red_cards', pyxb.binding.datatypes.byte)
    __red_cards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 156, 23)
    __red_cards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 156, 23)
    
    red_cards = property(__red_cards.value, __red_cards.set, None, None)

    
    # Attribute yellow-cards uses Python identifier yellow_cards
    __yellow_cards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'yellow-cards'), 'yellow_cards', '__AbsentNamespace0_CTD_ANON_15_yellow_cards', pyxb.binding.datatypes.byte)
    __yellow_cards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 157, 23)
    __yellow_cards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 157, 23)
    
    yellow_cards = property(__yellow_cards.value, __yellow_cards.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fouls_commited.name() : __fouls_commited,
        __fouls_suffered.name() : __fouls_suffered,
        __yellow_red_cards.name() : __yellow_red_cards,
        __red_cards.name() : __red_cards,
        __yellow_cards.name() : __yellow_cards
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 186, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element stats-time uses Python identifier stats_time
    __stats_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-time'), 'stats_time', '__AbsentNamespace0_CTD_ANON_16_stats_time', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 188, 19), )

    
    stats_time = property(__stats_time.value, __stats_time.set, None, None)

    
    # Element stats-ball uses Python identifier stats_ball
    __stats_ball = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-ball'), 'stats_ball', '__AbsentNamespace0_CTD_ANON_16_stats_ball', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 199, 19), )

    
    stats_ball = property(__stats_ball.value, __stats_ball.set, None, None)

    
    # Element stats-passes uses Python identifier stats_passes
    __stats_passes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-passes'), 'stats_passes', '__AbsentNamespace0_CTD_ANON_16_stats_passes', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 214, 19), )

    
    stats_passes = property(__stats_passes.value, __stats_passes.set, None, None)

    
    # Element stats-duels uses Python identifier stats_duels
    __stats_duels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-duels'), 'stats_duels', '__AbsentNamespace0_CTD_ANON_16_stats_duels', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 238, 19), )

    
    stats_duels = property(__stats_duels.value, __stats_duels.set, None, None)

    
    # Element stats-performance uses Python identifier stats_performance
    __stats_performance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-performance'), 'stats_performance', '__AbsentNamespace0_CTD_ANON_16_stats_performance', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 252, 19), )

    
    stats_performance = property(__stats_performance.value, __stats_performance.set, None, None)

    
    # Element stats-runs uses Python identifier stats_runs
    __stats_runs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-runs'), 'stats_runs', '__AbsentNamespace0_CTD_ANON_16_stats_runs', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 278, 19), )

    
    stats_runs = property(__stats_runs.value, __stats_runs.set, None, None)

    
    # Element stats-goalkeeper uses Python identifier stats_goalkeeper
    __stats_goalkeeper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stats-goalkeeper'), 'stats_goalkeeper', '__AbsentNamespace0_CTD_ANON_16_stats_goalkeeper', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 306, 19), )

    
    stats_goalkeeper = property(__stats_goalkeeper.value, __stats_goalkeeper.set, None, None)

    _ElementMap.update({
        __stats_time.name() : __stats_time,
        __stats_ball.name() : __stats_ball,
        __stats_passes.name() : __stats_passes,
        __stats_duels.name() : __stats_duels,
        __stats_performance.name() : __stats_performance,
        __stats_runs.name() : __stats_runs,
        __stats_goalkeeper.name() : __stats_goalkeeper
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 189, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute playedTime uses Python identifier playedTime
    __playedTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playedTime'), 'playedTime', '__AbsentNamespace0_CTD_ANON_17_playedTime', pyxb.binding.datatypes.float)
    __playedTime._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 192, 23)
    __playedTime._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 192, 23)
    
    playedTime = property(__playedTime.value, __playedTime.set, None, None)

    
    # Attribute playedTime_1HT uses Python identifier playedTime_1HT
    __playedTime_1HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playedTime_1HT'), 'playedTime_1HT', '__AbsentNamespace0_CTD_ANON_17_playedTime_1HT', pyxb.binding.datatypes.float)
    __playedTime_1HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 193, 23)
    __playedTime_1HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 193, 23)
    
    playedTime_1HT = property(__playedTime_1HT.value, __playedTime_1HT.set, None, None)

    
    # Attribute playedTime_2HT uses Python identifier playedTime_2HT
    __playedTime_2HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playedTime_2HT'), 'playedTime_2HT', '__AbsentNamespace0_CTD_ANON_17_playedTime_2HT', pyxb.binding.datatypes.float)
    __playedTime_2HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 194, 23)
    __playedTime_2HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 194, 23)
    
    playedTime_2HT = property(__playedTime_2HT.value, __playedTime_2HT.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __playedTime.name() : __playedTime,
        __playedTime_1HT.name() : __playedTime_1HT,
        __playedTime_2HT.name() : __playedTime_2HT
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 200, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute ballTouchesTotal uses Python identifier ballTouchesTotal
    __ballTouchesTotal = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballTouchesTotal'), 'ballTouchesTotal', '__AbsentNamespace0_CTD_ANON_18_ballTouchesTotal', pyxb.binding.datatypes.byte)
    __ballTouchesTotal._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 203, 23)
    __ballTouchesTotal._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 203, 23)
    
    ballTouchesTotal = property(__ballTouchesTotal.value, __ballTouchesTotal.set, None, None)

    
    # Attribute ballTouch_OwnHalf uses Python identifier ballTouch_OwnHalf
    __ballTouch_OwnHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballTouch_OwnHalf'), 'ballTouch_OwnHalf', '__AbsentNamespace0_CTD_ANON_18_ballTouch_OwnHalf', pyxb.binding.datatypes.byte)
    __ballTouch_OwnHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 204, 23)
    __ballTouch_OwnHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 204, 23)
    
    ballTouch_OwnHalf = property(__ballTouch_OwnHalf.value, __ballTouch_OwnHalf.set, None, None)

    
    # Attribute ballTouch_OpposingHalf uses Python identifier ballTouch_OpposingHalf
    __ballTouch_OpposingHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballTouch_OpposingHalf'), 'ballTouch_OpposingHalf', '__AbsentNamespace0_CTD_ANON_18_ballTouch_OpposingHalf', pyxb.binding.datatypes.byte)
    __ballTouch_OpposingHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 205, 23)
    __ballTouch_OpposingHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 205, 23)
    
    ballTouch_OpposingHalf = property(__ballTouch_OpposingHalf.value, __ballTouch_OpposingHalf.set, None, None)

    
    # Attribute ballTouch_OwnPenaltyArea uses Python identifier ballTouch_OwnPenaltyArea
    __ballTouch_OwnPenaltyArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballTouch_OwnPenaltyArea'), 'ballTouch_OwnPenaltyArea', '__AbsentNamespace0_CTD_ANON_18_ballTouch_OwnPenaltyArea', pyxb.binding.datatypes.byte)
    __ballTouch_OwnPenaltyArea._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 206, 23)
    __ballTouch_OwnPenaltyArea._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 206, 23)
    
    ballTouch_OwnPenaltyArea = property(__ballTouch_OwnPenaltyArea.value, __ballTouch_OwnPenaltyArea.set, None, None)

    
    # Attribute ballTouch_OpposingPenaltyArea uses Python identifier ballTouch_OpposingPenaltyArea
    __ballTouch_OpposingPenaltyArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballTouch_OpposingPenaltyArea'), 'ballTouch_OpposingPenaltyArea', '__AbsentNamespace0_CTD_ANON_18_ballTouch_OpposingPenaltyArea', pyxb.binding.datatypes.byte)
    __ballTouch_OpposingPenaltyArea._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 207, 23)
    __ballTouch_OpposingPenaltyArea._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 207, 23)
    
    ballTouch_OpposingPenaltyArea = property(__ballTouch_OpposingPenaltyArea.value, __ballTouch_OpposingPenaltyArea.set, None, None)

    
    # Attribute ballPossessionTime uses Python identifier ballPossessionTime
    __ballPossessionTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ballPossessionTime'), 'ballPossessionTime', '__AbsentNamespace0_CTD_ANON_18_ballPossessionTime', pyxb.binding.datatypes.float)
    __ballPossessionTime._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 208, 23)
    __ballPossessionTime._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 208, 23)
    
    ballPossessionTime = property(__ballPossessionTime.value, __ballPossessionTime.set, None, None)

    
    # Attribute avgDistance_ToBall uses Python identifier avgDistance_ToBall
    __avgDistance_ToBall = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_ToBall'), 'avgDistance_ToBall', '__AbsentNamespace0_CTD_ANON_18_avgDistance_ToBall', pyxb.binding.datatypes.float)
    __avgDistance_ToBall._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 209, 23)
    __avgDistance_ToBall._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 209, 23)
    
    avgDistance_ToBall = property(__avgDistance_ToBall.value, __avgDistance_ToBall.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ballTouchesTotal.name() : __ballTouchesTotal,
        __ballTouch_OwnHalf.name() : __ballTouch_OwnHalf,
        __ballTouch_OpposingHalf.name() : __ballTouch_OpposingHalf,
        __ballTouch_OwnPenaltyArea.name() : __ballTouch_OwnPenaltyArea,
        __ballTouch_OpposingPenaltyArea.name() : __ballTouch_OpposingPenaltyArea,
        __ballPossessionTime.name() : __ballPossessionTime,
        __avgDistance_ToBall.name() : __avgDistance_ToBall
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 215, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute passesTotal uses Python identifier passesTotal
    __passesTotal = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passesTotal'), 'passesTotal', '__AbsentNamespace0_CTD_ANON_19_passesTotal', pyxb.binding.datatypes.byte)
    __passesTotal._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 218, 23)
    __passesTotal._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 218, 23)
    
    passesTotal = property(__passesTotal.value, __passesTotal.set, None, None)

    
    # Attribute passesTotal_Completed uses Python identifier passesTotal_Completed
    __passesTotal_Completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passesTotal_Completed'), 'passesTotal_Completed', '__AbsentNamespace0_CTD_ANON_19_passesTotal_Completed', pyxb.binding.datatypes.byte)
    __passesTotal_Completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 219, 23)
    __passesTotal_Completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 219, 23)
    
    passesTotal_Completed = property(__passesTotal_Completed.value, __passesTotal_Completed.set, None, None)

    
    # Attribute squarePasses uses Python identifier squarePasses
    __squarePasses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'squarePasses'), 'squarePasses', '__AbsentNamespace0_CTD_ANON_19_squarePasses', pyxb.binding.datatypes.byte)
    __squarePasses._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 220, 23)
    __squarePasses._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 220, 23)
    
    squarePasses = property(__squarePasses.value, __squarePasses.set, None, None)

    
    # Attribute squarePasses_Completed uses Python identifier squarePasses_Completed
    __squarePasses_Completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'squarePasses_Completed'), 'squarePasses_Completed', '__AbsentNamespace0_CTD_ANON_19_squarePasses_Completed', pyxb.binding.datatypes.byte)
    __squarePasses_Completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 221, 23)
    __squarePasses_Completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 221, 23)
    
    squarePasses_Completed = property(__squarePasses_Completed.value, __squarePasses_Completed.set, None, None)

    
    # Attribute troughBallPasses uses Python identifier troughBallPasses
    __troughBallPasses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'troughBallPasses'), 'troughBallPasses', '__AbsentNamespace0_CTD_ANON_19_troughBallPasses', pyxb.binding.datatypes.byte)
    __troughBallPasses._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 222, 23)
    __troughBallPasses._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 222, 23)
    
    troughBallPasses = property(__troughBallPasses.value, __troughBallPasses.set, None, None)

    
    # Attribute troughBallPasses_Completed uses Python identifier troughBallPasses_Completed
    __troughBallPasses_Completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'troughBallPasses_Completed'), 'troughBallPasses_Completed', '__AbsentNamespace0_CTD_ANON_19_troughBallPasses_Completed', pyxb.binding.datatypes.byte)
    __troughBallPasses_Completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 223, 23)
    __troughBallPasses_Completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 223, 23)
    
    troughBallPasses_Completed = property(__troughBallPasses_Completed.value, __troughBallPasses_Completed.set, None, None)

    
    # Attribute diagonalPasses uses Python identifier diagonalPasses
    __diagonalPasses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'diagonalPasses'), 'diagonalPasses', '__AbsentNamespace0_CTD_ANON_19_diagonalPasses', pyxb.binding.datatypes.byte)
    __diagonalPasses._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 224, 23)
    __diagonalPasses._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 224, 23)
    
    diagonalPasses = property(__diagonalPasses.value, __diagonalPasses.set, None, None)

    
    # Attribute diagonalPasses_Completed uses Python identifier diagonalPasses_Completed
    __diagonalPasses_Completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'diagonalPasses_Completed'), 'diagonalPasses_Completed', '__AbsentNamespace0_CTD_ANON_19_diagonalPasses_Completed', pyxb.binding.datatypes.byte)
    __diagonalPasses_Completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 225, 23)
    __diagonalPasses_Completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 225, 23)
    
    diagonalPasses_Completed = property(__diagonalPasses_Completed.value, __diagonalPasses_Completed.set, None, None)

    
    # Attribute backPasses uses Python identifier backPasses
    __backPasses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'backPasses'), 'backPasses', '__AbsentNamespace0_CTD_ANON_19_backPasses', pyxb.binding.datatypes.byte)
    __backPasses._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 226, 23)
    __backPasses._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 226, 23)
    
    backPasses = property(__backPasses.value, __backPasses.set, None, None)

    
    # Attribute backPasses_Completed uses Python identifier backPasses_Completed
    __backPasses_Completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'backPasses_Completed'), 'backPasses_Completed', '__AbsentNamespace0_CTD_ANON_19_backPasses_Completed', pyxb.binding.datatypes.byte)
    __backPasses_Completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 227, 23)
    __backPasses_Completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 227, 23)
    
    backPasses_Completed = property(__backPasses_Completed.value, __backPasses_Completed.set, None, None)

    
    # Attribute passesIntoOffensiveArea uses Python identifier passesIntoOffensiveArea
    __passesIntoOffensiveArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passesIntoOffensiveArea'), 'passesIntoOffensiveArea', '__AbsentNamespace0_CTD_ANON_19_passesIntoOffensiveArea', pyxb.binding.datatypes.byte)
    __passesIntoOffensiveArea._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 228, 23)
    __passesIntoOffensiveArea._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 228, 23)
    
    passesIntoOffensiveArea = property(__passesIntoOffensiveArea.value, __passesIntoOffensiveArea.set, None, None)

    
    # Attribute passesIntoOffensiveArea_Completed uses Python identifier passesIntoOffensiveArea_Completed
    __passesIntoOffensiveArea_Completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passesIntoOffensiveArea_Completed'), 'passesIntoOffensiveArea_Completed', '__AbsentNamespace0_CTD_ANON_19_passesIntoOffensiveArea_Completed', pyxb.binding.datatypes.byte)
    __passesIntoOffensiveArea_Completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 229, 23)
    __passesIntoOffensiveArea_Completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 229, 23)
    
    passesIntoOffensiveArea_Completed = property(__passesIntoOffensiveArea_Completed.value, __passesIntoOffensiveArea_Completed.set, None, None)

    
    # Attribute passes_OwnHalf uses Python identifier passes_OwnHalf
    __passes_OwnHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes_OwnHalf'), 'passes_OwnHalf', '__AbsentNamespace0_CTD_ANON_19_passes_OwnHalf', pyxb.binding.datatypes.byte)
    __passes_OwnHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 230, 23)
    __passes_OwnHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 230, 23)
    
    passes_OwnHalf = property(__passes_OwnHalf.value, __passes_OwnHalf.set, None, None)

    
    # Attribute passes_OwnHalf_Completed uses Python identifier passes_OwnHalf_Completed
    __passes_OwnHalf_Completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes_OwnHalf_Completed'), 'passes_OwnHalf_Completed', '__AbsentNamespace0_CTD_ANON_19_passes_OwnHalf_Completed', pyxb.binding.datatypes.byte)
    __passes_OwnHalf_Completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 231, 23)
    __passes_OwnHalf_Completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 231, 23)
    
    passes_OwnHalf_Completed = property(__passes_OwnHalf_Completed.value, __passes_OwnHalf_Completed.set, None, None)

    
    # Attribute passes_OpposingHalf uses Python identifier passes_OpposingHalf
    __passes_OpposingHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes_OpposingHalf'), 'passes_OpposingHalf', '__AbsentNamespace0_CTD_ANON_19_passes_OpposingHalf', pyxb.binding.datatypes.byte)
    __passes_OpposingHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 232, 23)
    __passes_OpposingHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 232, 23)
    
    passes_OpposingHalf = property(__passes_OpposingHalf.value, __passes_OpposingHalf.set, None, None)

    
    # Attribute passes_OpposingHalf_Completed uses Python identifier passes_OpposingHalf_Completed
    __passes_OpposingHalf_Completed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'passes_OpposingHalf_Completed'), 'passes_OpposingHalf_Completed', '__AbsentNamespace0_CTD_ANON_19_passes_OpposingHalf_Completed', pyxb.binding.datatypes.byte)
    __passes_OpposingHalf_Completed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 233, 23)
    __passes_OpposingHalf_Completed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 233, 23)
    
    passes_OpposingHalf_Completed = property(__passes_OpposingHalf_Completed.value, __passes_OpposingHalf_Completed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __passesTotal.name() : __passesTotal,
        __passesTotal_Completed.name() : __passesTotal_Completed,
        __squarePasses.name() : __squarePasses,
        __squarePasses_Completed.name() : __squarePasses_Completed,
        __troughBallPasses.name() : __troughBallPasses,
        __troughBallPasses_Completed.name() : __troughBallPasses_Completed,
        __diagonalPasses.name() : __diagonalPasses,
        __diagonalPasses_Completed.name() : __diagonalPasses_Completed,
        __backPasses.name() : __backPasses,
        __backPasses_Completed.name() : __backPasses_Completed,
        __passesIntoOffensiveArea.name() : __passesIntoOffensiveArea,
        __passesIntoOffensiveArea_Completed.name() : __passesIntoOffensiveArea_Completed,
        __passes_OwnHalf.name() : __passes_OwnHalf,
        __passes_OwnHalf_Completed.name() : __passes_OwnHalf_Completed,
        __passes_OpposingHalf.name() : __passes_OpposingHalf,
        __passes_OpposingHalf_Completed.name() : __passes_OpposingHalf_Completed
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 239, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute duels_Defensive_OpposingHalf uses Python identifier duels_Defensive_OpposingHalf
    __duels_Defensive_OpposingHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels_Defensive_OpposingHalf'), 'duels_Defensive_OpposingHalf', '__AbsentNamespace0_CTD_ANON_20_duels_Defensive_OpposingHalf', pyxb.binding.datatypes.byte)
    __duels_Defensive_OpposingHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 242, 23)
    __duels_Defensive_OpposingHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 242, 23)
    
    duels_Defensive_OpposingHalf = property(__duels_Defensive_OpposingHalf.value, __duels_Defensive_OpposingHalf.set, None, None)

    
    # Attribute duels_Defensive_OpposingHalf_Won uses Python identifier duels_Defensive_OpposingHalf_Won
    __duels_Defensive_OpposingHalf_Won = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels_Defensive_OpposingHalf_Won'), 'duels_Defensive_OpposingHalf_Won', '__AbsentNamespace0_CTD_ANON_20_duels_Defensive_OpposingHalf_Won', pyxb.binding.datatypes.byte)
    __duels_Defensive_OpposingHalf_Won._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 243, 23)
    __duels_Defensive_OpposingHalf_Won._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 243, 23)
    
    duels_Defensive_OpposingHalf_Won = property(__duels_Defensive_OpposingHalf_Won.value, __duels_Defensive_OpposingHalf_Won.set, None, None)

    
    # Attribute duels_OppoosingPenaltyArea uses Python identifier duels_OppoosingPenaltyArea
    __duels_OppoosingPenaltyArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels_OppoosingPenaltyArea'), 'duels_OppoosingPenaltyArea', '__AbsentNamespace0_CTD_ANON_20_duels_OppoosingPenaltyArea', pyxb.binding.datatypes.byte)
    __duels_OppoosingPenaltyArea._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 244, 23)
    __duels_OppoosingPenaltyArea._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 244, 23)
    
    duels_OppoosingPenaltyArea = property(__duels_OppoosingPenaltyArea.value, __duels_OppoosingPenaltyArea.set, None, None)

    
    # Attribute duels_OppoosingPenaltyArea_Won uses Python identifier duels_OppoosingPenaltyArea_Won
    __duels_OppoosingPenaltyArea_Won = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels_OppoosingPenaltyArea_Won'), 'duels_OppoosingPenaltyArea_Won', '__AbsentNamespace0_CTD_ANON_20_duels_OppoosingPenaltyArea_Won', pyxb.binding.datatypes.byte)
    __duels_OppoosingPenaltyArea_Won._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 245, 23)
    __duels_OppoosingPenaltyArea_Won._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 245, 23)
    
    duels_OppoosingPenaltyArea_Won = property(__duels_OppoosingPenaltyArea_Won.value, __duels_OppoosingPenaltyArea_Won.set, None, None)

    
    # Attribute duels_OwnPenaltyArea uses Python identifier duels_OwnPenaltyArea
    __duels_OwnPenaltyArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels_OwnPenaltyArea'), 'duels_OwnPenaltyArea', '__AbsentNamespace0_CTD_ANON_20_duels_OwnPenaltyArea', pyxb.binding.datatypes.byte)
    __duels_OwnPenaltyArea._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 246, 23)
    __duels_OwnPenaltyArea._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 246, 23)
    
    duels_OwnPenaltyArea = property(__duels_OwnPenaltyArea.value, __duels_OwnPenaltyArea.set, None, None)

    
    # Attribute duels_OwnPenaltyArea_Won uses Python identifier duels_OwnPenaltyArea_Won
    __duels_OwnPenaltyArea_Won = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duels_OwnPenaltyArea_Won'), 'duels_OwnPenaltyArea_Won', '__AbsentNamespace0_CTD_ANON_20_duels_OwnPenaltyArea_Won', pyxb.binding.datatypes.byte)
    __duels_OwnPenaltyArea_Won._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 247, 23)
    __duels_OwnPenaltyArea_Won._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 247, 23)
    
    duels_OwnPenaltyArea_Won = property(__duels_OwnPenaltyArea_Won.value, __duels_OwnPenaltyArea_Won.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duels_Defensive_OpposingHalf.name() : __duels_Defensive_OpposingHalf,
        __duels_Defensive_OpposingHalf_Won.name() : __duels_Defensive_OpposingHalf_Won,
        __duels_OppoosingPenaltyArea.name() : __duels_OppoosingPenaltyArea,
        __duels_OppoosingPenaltyArea_Won.name() : __duels_OppoosingPenaltyArea_Won,
        __duels_OwnPenaltyArea.name() : __duels_OwnPenaltyArea,
        __duels_OwnPenaltyArea_Won.name() : __duels_OwnPenaltyArea_Won
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 253, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute distance uses Python identifier distance
    __distance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance'), 'distance', '__AbsentNamespace0_CTD_ANON_21_distance', pyxb.binding.datatypes.float)
    __distance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 256, 23)
    __distance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 256, 23)
    
    distance = property(__distance.value, __distance.set, None, None)

    
    # Attribute distance_1HT uses Python identifier distance_1HT
    __distance_1HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_1HT'), 'distance_1HT', '__AbsentNamespace0_CTD_ANON_21_distance_1HT', pyxb.binding.datatypes.float)
    __distance_1HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 257, 23)
    __distance_1HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 257, 23)
    
    distance_1HT = property(__distance_1HT.value, __distance_1HT.set, None, None)

    
    # Attribute distance_2HT uses Python identifier distance_2HT
    __distance_2HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_2HT'), 'distance_2HT', '__AbsentNamespace0_CTD_ANON_21_distance_2HT', pyxb.binding.datatypes.float)
    __distance_2HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 258, 23)
    __distance_2HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 258, 23)
    
    distance_2HT = property(__distance_2HT.value, __distance_2HT.set, None, None)

    
    # Attribute distance_Last15Minutes uses Python identifier distance_Last15Minutes
    __distance_Last15Minutes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_Last15Minutes'), 'distance_Last15Minutes', '__AbsentNamespace0_CTD_ANON_21_distance_Last15Minutes', pyxb.binding.datatypes.float)
    __distance_Last15Minutes._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 259, 23)
    __distance_Last15Minutes._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 259, 23)
    
    distance_Last15Minutes = property(__distance_Last15Minutes.value, __distance_Last15Minutes.set, None, None)

    
    # Attribute playedTime_Last15Minutes uses Python identifier playedTime_Last15Minutes
    __playedTime_Last15Minutes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playedTime_Last15Minutes'), 'playedTime_Last15Minutes', '__AbsentNamespace0_CTD_ANON_21_playedTime_Last15Minutes', pyxb.binding.datatypes.float)
    __playedTime_Last15Minutes._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 260, 23)
    __playedTime_Last15Minutes._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 260, 23)
    
    playedTime_Last15Minutes = property(__playedTime_Last15Minutes.value, __playedTime_Last15Minutes.set, None, None)

    
    # Attribute distance_OwnHalf uses Python identifier distance_OwnHalf
    __distance_OwnHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_OwnHalf'), 'distance_OwnHalf', '__AbsentNamespace0_CTD_ANON_21_distance_OwnHalf', pyxb.binding.datatypes.float)
    __distance_OwnHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 261, 23)
    __distance_OwnHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 261, 23)
    
    distance_OwnHalf = property(__distance_OwnHalf.value, __distance_OwnHalf.set, None, None)

    
    # Attribute distance_OwnHalf_1HT uses Python identifier distance_OwnHalf_1HT
    __distance_OwnHalf_1HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_OwnHalf_1HT'), 'distance_OwnHalf_1HT', '__AbsentNamespace0_CTD_ANON_21_distance_OwnHalf_1HT', pyxb.binding.datatypes.float)
    __distance_OwnHalf_1HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 262, 23)
    __distance_OwnHalf_1HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 262, 23)
    
    distance_OwnHalf_1HT = property(__distance_OwnHalf_1HT.value, __distance_OwnHalf_1HT.set, None, None)

    
    # Attribute distance_OwnHalf_2HT uses Python identifier distance_OwnHalf_2HT
    __distance_OwnHalf_2HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_OwnHalf_2HT'), 'distance_OwnHalf_2HT', '__AbsentNamespace0_CTD_ANON_21_distance_OwnHalf_2HT', pyxb.binding.datatypes.float)
    __distance_OwnHalf_2HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 263, 23)
    __distance_OwnHalf_2HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 263, 23)
    
    distance_OwnHalf_2HT = property(__distance_OwnHalf_2HT.value, __distance_OwnHalf_2HT.set, None, None)

    
    # Attribute distance_OpposingHalf uses Python identifier distance_OpposingHalf
    __distance_OpposingHalf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_OpposingHalf'), 'distance_OpposingHalf', '__AbsentNamespace0_CTD_ANON_21_distance_OpposingHalf', pyxb.binding.datatypes.float)
    __distance_OpposingHalf._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 264, 23)
    __distance_OpposingHalf._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 264, 23)
    
    distance_OpposingHalf = property(__distance_OpposingHalf.value, __distance_OpposingHalf.set, None, None)

    
    # Attribute distance_OpposingHalf_1HT uses Python identifier distance_OpposingHalf_1HT
    __distance_OpposingHalf_1HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_OpposingHalf_1HT'), 'distance_OpposingHalf_1HT', '__AbsentNamespace0_CTD_ANON_21_distance_OpposingHalf_1HT', pyxb.binding.datatypes.float)
    __distance_OpposingHalf_1HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 265, 23)
    __distance_OpposingHalf_1HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 265, 23)
    
    distance_OpposingHalf_1HT = property(__distance_OpposingHalf_1HT.value, __distance_OpposingHalf_1HT.set, None, None)

    
    # Attribute distance_OpposingHalf_2HT uses Python identifier distance_OpposingHalf_2HT
    __distance_OpposingHalf_2HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_OpposingHalf_2HT'), 'distance_OpposingHalf_2HT', '__AbsentNamespace0_CTD_ANON_21_distance_OpposingHalf_2HT', pyxb.binding.datatypes.float)
    __distance_OpposingHalf_2HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 266, 23)
    __distance_OpposingHalf_2HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 266, 23)
    
    distance_OpposingHalf_2HT = property(__distance_OpposingHalf_2HT.value, __distance_OpposingHalf_2HT.set, None, None)

    
    # Attribute distance_BallInPossesion uses Python identifier distance_BallInPossesion
    __distance_BallInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_BallInPossesion'), 'distance_BallInPossesion', '__AbsentNamespace0_CTD_ANON_21_distance_BallInPossesion', pyxb.binding.datatypes.float)
    __distance_BallInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 267, 23)
    __distance_BallInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 267, 23)
    
    distance_BallInPossesion = property(__distance_BallInPossesion.value, __distance_BallInPossesion.set, None, None)

    
    # Attribute distance_BallInPossesion_1HT uses Python identifier distance_BallInPossesion_1HT
    __distance_BallInPossesion_1HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_BallInPossesion_1HT'), 'distance_BallInPossesion_1HT', '__AbsentNamespace0_CTD_ANON_21_distance_BallInPossesion_1HT', pyxb.binding.datatypes.float)
    __distance_BallInPossesion_1HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 268, 23)
    __distance_BallInPossesion_1HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 268, 23)
    
    distance_BallInPossesion_1HT = property(__distance_BallInPossesion_1HT.value, __distance_BallInPossesion_1HT.set, None, None)

    
    # Attribute distance_BallInPossesion_2HT uses Python identifier distance_BallInPossesion_2HT
    __distance_BallInPossesion_2HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_BallInPossesion_2HT'), 'distance_BallInPossesion_2HT', '__AbsentNamespace0_CTD_ANON_21_distance_BallInPossesion_2HT', pyxb.binding.datatypes.float)
    __distance_BallInPossesion_2HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 269, 23)
    __distance_BallInPossesion_2HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 269, 23)
    
    distance_BallInPossesion_2HT = property(__distance_BallInPossesion_2HT.value, __distance_BallInPossesion_2HT.set, None, None)

    
    # Attribute distance_BallNotInPossesion uses Python identifier distance_BallNotInPossesion
    __distance_BallNotInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_BallNotInPossesion'), 'distance_BallNotInPossesion', '__AbsentNamespace0_CTD_ANON_21_distance_BallNotInPossesion', pyxb.binding.datatypes.float)
    __distance_BallNotInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 270, 23)
    __distance_BallNotInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 270, 23)
    
    distance_BallNotInPossesion = property(__distance_BallNotInPossesion.value, __distance_BallNotInPossesion.set, None, None)

    
    # Attribute distance_BallNotInPossesion_1HT uses Python identifier distance_BallNotInPossesion_1HT
    __distance_BallNotInPossesion_1HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_BallNotInPossesion_1HT'), 'distance_BallNotInPossesion_1HT', '__AbsentNamespace0_CTD_ANON_21_distance_BallNotInPossesion_1HT', pyxb.binding.datatypes.float)
    __distance_BallNotInPossesion_1HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 271, 23)
    __distance_BallNotInPossesion_1HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 271, 23)
    
    distance_BallNotInPossesion_1HT = property(__distance_BallNotInPossesion_1HT.value, __distance_BallNotInPossesion_1HT.set, None, None)

    
    # Attribute distance_BallNotInPossesion_2HT uses Python identifier distance_BallNotInPossesion_2HT
    __distance_BallNotInPossesion_2HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance_BallNotInPossesion_2HT'), 'distance_BallNotInPossesion_2HT', '__AbsentNamespace0_CTD_ANON_21_distance_BallNotInPossesion_2HT', pyxb.binding.datatypes.float)
    __distance_BallNotInPossesion_2HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 272, 23)
    __distance_BallNotInPossesion_2HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 272, 23)
    
    distance_BallNotInPossesion_2HT = property(__distance_BallNotInPossesion_2HT.value, __distance_BallNotInPossesion_2HT.set, None, None)

    
    # Attribute maxSpeed uses Python identifier maxSpeed
    __maxSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxSpeed'), 'maxSpeed', '__AbsentNamespace0_CTD_ANON_21_maxSpeed', pyxb.binding.datatypes.float)
    __maxSpeed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 273, 23)
    __maxSpeed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 273, 23)
    
    maxSpeed = property(__maxSpeed.value, __maxSpeed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __distance.name() : __distance,
        __distance_1HT.name() : __distance_1HT,
        __distance_2HT.name() : __distance_2HT,
        __distance_Last15Minutes.name() : __distance_Last15Minutes,
        __playedTime_Last15Minutes.name() : __playedTime_Last15Minutes,
        __distance_OwnHalf.name() : __distance_OwnHalf,
        __distance_OwnHalf_1HT.name() : __distance_OwnHalf_1HT,
        __distance_OwnHalf_2HT.name() : __distance_OwnHalf_2HT,
        __distance_OpposingHalf.name() : __distance_OpposingHalf,
        __distance_OpposingHalf_1HT.name() : __distance_OpposingHalf_1HT,
        __distance_OpposingHalf_2HT.name() : __distance_OpposingHalf_2HT,
        __distance_BallInPossesion.name() : __distance_BallInPossesion,
        __distance_BallInPossesion_1HT.name() : __distance_BallInPossesion_1HT,
        __distance_BallInPossesion_2HT.name() : __distance_BallInPossesion_2HT,
        __distance_BallNotInPossesion.name() : __distance_BallNotInPossesion,
        __distance_BallNotInPossesion_1HT.name() : __distance_BallNotInPossesion_1HT,
        __distance_BallNotInPossesion_2HT.name() : __distance_BallNotInPossesion_2HT,
        __maxSpeed.name() : __maxSpeed
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 279, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute sprints uses Python identifier sprints
    __sprints = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sprints'), 'sprints', '__AbsentNamespace0_CTD_ANON_22_sprints', pyxb.binding.datatypes.byte)
    __sprints._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 282, 23)
    __sprints._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 282, 23)
    
    sprints = property(__sprints.value, __sprints.set, None, None)

    
    # Attribute sprints_Distance uses Python identifier sprints_Distance
    __sprints_Distance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sprints_Distance'), 'sprints_Distance', '__AbsentNamespace0_CTD_ANON_22_sprints_Distance', pyxb.binding.datatypes.float)
    __sprints_Distance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 283, 23)
    __sprints_Distance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 283, 23)
    
    sprints_Distance = property(__sprints_Distance.value, __sprints_Distance.set, None, None)

    
    # Attribute sprints_1HT uses Python identifier sprints_1HT
    __sprints_1HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sprints_1HT'), 'sprints_1HT', '__AbsentNamespace0_CTD_ANON_22_sprints_1HT', pyxb.binding.datatypes.byte)
    __sprints_1HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 284, 23)
    __sprints_1HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 284, 23)
    
    sprints_1HT = property(__sprints_1HT.value, __sprints_1HT.set, None, None)

    
    # Attribute sprints_2HT uses Python identifier sprints_2HT
    __sprints_2HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sprints_2HT'), 'sprints_2HT', '__AbsentNamespace0_CTD_ANON_22_sprints_2HT', pyxb.binding.datatypes.byte)
    __sprints_2HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 285, 23)
    __sprints_2HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 285, 23)
    
    sprints_2HT = property(__sprints_2HT.value, __sprints_2HT.set, None, None)

    
    # Attribute sprints_Forwards uses Python identifier sprints_Forwards
    __sprints_Forwards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sprints_Forwards'), 'sprints_Forwards', '__AbsentNamespace0_CTD_ANON_22_sprints_Forwards', pyxb.binding.datatypes.byte)
    __sprints_Forwards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 286, 23)
    __sprints_Forwards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 286, 23)
    
    sprints_Forwards = property(__sprints_Forwards.value, __sprints_Forwards.set, None, None)

    
    # Attribute sprints_Backwards uses Python identifier sprints_Backwards
    __sprints_Backwards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sprints_Backwards'), 'sprints_Backwards', '__AbsentNamespace0_CTD_ANON_22_sprints_Backwards', pyxb.binding.datatypes.byte)
    __sprints_Backwards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 287, 23)
    __sprints_Backwards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 287, 23)
    
    sprints_Backwards = property(__sprints_Backwards.value, __sprints_Backwards.set, None, None)

    
    # Attribute sprints_BallInPossesion uses Python identifier sprints_BallInPossesion
    __sprints_BallInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sprints_BallInPossesion'), 'sprints_BallInPossesion', '__AbsentNamespace0_CTD_ANON_22_sprints_BallInPossesion', pyxb.binding.datatypes.byte)
    __sprints_BallInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 288, 23)
    __sprints_BallInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 288, 23)
    
    sprints_BallInPossesion = property(__sprints_BallInPossesion.value, __sprints_BallInPossesion.set, None, None)

    
    # Attribute sprints_BallNotInPossesion uses Python identifier sprints_BallNotInPossesion
    __sprints_BallNotInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sprints_BallNotInPossesion'), 'sprints_BallNotInPossesion', '__AbsentNamespace0_CTD_ANON_22_sprints_BallNotInPossesion', pyxb.binding.datatypes.byte)
    __sprints_BallNotInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 289, 23)
    __sprints_BallNotInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 289, 23)
    
    sprints_BallNotInPossesion = property(__sprints_BallNotInPossesion.value, __sprints_BallNotInPossesion.set, None, None)

    
    # Attribute fastRuns uses Python identifier fastRuns
    __fastRuns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fastRuns'), 'fastRuns', '__AbsentNamespace0_CTD_ANON_22_fastRuns', pyxb.binding.datatypes.byte)
    __fastRuns._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 290, 23)
    __fastRuns._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 290, 23)
    
    fastRuns = property(__fastRuns.value, __fastRuns.set, None, None)

    
    # Attribute fastRuns_Distance uses Python identifier fastRuns_Distance
    __fastRuns_Distance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fastRuns_Distance'), 'fastRuns_Distance', '__AbsentNamespace0_CTD_ANON_22_fastRuns_Distance', pyxb.binding.datatypes.float)
    __fastRuns_Distance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 291, 23)
    __fastRuns_Distance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 291, 23)
    
    fastRuns_Distance = property(__fastRuns_Distance.value, __fastRuns_Distance.set, None, None)

    
    # Attribute fastRuns_1HT uses Python identifier fastRuns_1HT
    __fastRuns_1HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fastRuns_1HT'), 'fastRuns_1HT', '__AbsentNamespace0_CTD_ANON_22_fastRuns_1HT', pyxb.binding.datatypes.byte)
    __fastRuns_1HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 292, 23)
    __fastRuns_1HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 292, 23)
    
    fastRuns_1HT = property(__fastRuns_1HT.value, __fastRuns_1HT.set, None, None)

    
    # Attribute fastRuns_2HT uses Python identifier fastRuns_2HT
    __fastRuns_2HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fastRuns_2HT'), 'fastRuns_2HT', '__AbsentNamespace0_CTD_ANON_22_fastRuns_2HT', pyxb.binding.datatypes.byte)
    __fastRuns_2HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 293, 23)
    __fastRuns_2HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 293, 23)
    
    fastRuns_2HT = property(__fastRuns_2HT.value, __fastRuns_2HT.set, None, None)

    
    # Attribute fastRuns_Forwards uses Python identifier fastRuns_Forwards
    __fastRuns_Forwards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fastRuns_Forwards'), 'fastRuns_Forwards', '__AbsentNamespace0_CTD_ANON_22_fastRuns_Forwards', pyxb.binding.datatypes.byte)
    __fastRuns_Forwards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 294, 23)
    __fastRuns_Forwards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 294, 23)
    
    fastRuns_Forwards = property(__fastRuns_Forwards.value, __fastRuns_Forwards.set, None, None)

    
    # Attribute fastRuns_Backwards uses Python identifier fastRuns_Backwards
    __fastRuns_Backwards = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fastRuns_Backwards'), 'fastRuns_Backwards', '__AbsentNamespace0_CTD_ANON_22_fastRuns_Backwards', pyxb.binding.datatypes.byte)
    __fastRuns_Backwards._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 295, 23)
    __fastRuns_Backwards._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 295, 23)
    
    fastRuns_Backwards = property(__fastRuns_Backwards.value, __fastRuns_Backwards.set, None, None)

    
    # Attribute fastRuns_BallInPossesion uses Python identifier fastRuns_BallInPossesion
    __fastRuns_BallInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fastRuns_BallInPossesion'), 'fastRuns_BallInPossesion', '__AbsentNamespace0_CTD_ANON_22_fastRuns_BallInPossesion', pyxb.binding.datatypes.byte)
    __fastRuns_BallInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 296, 23)
    __fastRuns_BallInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 296, 23)
    
    fastRuns_BallInPossesion = property(__fastRuns_BallInPossesion.value, __fastRuns_BallInPossesion.set, None, None)

    
    # Attribute fastRuns_BallNotInPossesion uses Python identifier fastRuns_BallNotInPossesion
    __fastRuns_BallNotInPossesion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fastRuns_BallNotInPossesion'), 'fastRuns_BallNotInPossesion', '__AbsentNamespace0_CTD_ANON_22_fastRuns_BallNotInPossesion', pyxb.binding.datatypes.byte)
    __fastRuns_BallNotInPossesion._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 297, 23)
    __fastRuns_BallNotInPossesion._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 297, 23)
    
    fastRuns_BallNotInPossesion = property(__fastRuns_BallNotInPossesion.value, __fastRuns_BallNotInPossesion.set, None, None)

    
    # Attribute offensiveRuns uses Python identifier offensiveRuns
    __offensiveRuns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offensiveRuns'), 'offensiveRuns', '__AbsentNamespace0_CTD_ANON_22_offensiveRuns', pyxb.binding.datatypes.byte)
    __offensiveRuns._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 298, 23)
    __offensiveRuns._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 298, 23)
    
    offensiveRuns = property(__offensiveRuns.value, __offensiveRuns.set, None, None)

    
    # Attribute offensiveRuns_Distance uses Python identifier offensiveRuns_Distance
    __offensiveRuns_Distance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offensiveRuns_Distance'), 'offensiveRuns_Distance', '__AbsentNamespace0_CTD_ANON_22_offensiveRuns_Distance', pyxb.binding.datatypes.float)
    __offensiveRuns_Distance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 299, 23)
    __offensiveRuns_Distance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 299, 23)
    
    offensiveRuns_Distance = property(__offensiveRuns_Distance.value, __offensiveRuns_Distance.set, None, None)

    
    # Attribute offensiveRuns_1HT uses Python identifier offensiveRuns_1HT
    __offensiveRuns_1HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offensiveRuns_1HT'), 'offensiveRuns_1HT', '__AbsentNamespace0_CTD_ANON_22_offensiveRuns_1HT', pyxb.binding.datatypes.byte)
    __offensiveRuns_1HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 300, 23)
    __offensiveRuns_1HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 300, 23)
    
    offensiveRuns_1HT = property(__offensiveRuns_1HT.value, __offensiveRuns_1HT.set, None, None)

    
    # Attribute offensiveRuns_2HT uses Python identifier offensiveRuns_2HT
    __offensiveRuns_2HT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offensiveRuns_2HT'), 'offensiveRuns_2HT', '__AbsentNamespace0_CTD_ANON_22_offensiveRuns_2HT', pyxb.binding.datatypes.byte)
    __offensiveRuns_2HT._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 301, 23)
    __offensiveRuns_2HT._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 301, 23)
    
    offensiveRuns_2HT = property(__offensiveRuns_2HT.value, __offensiveRuns_2HT.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __sprints.name() : __sprints,
        __sprints_Distance.name() : __sprints_Distance,
        __sprints_1HT.name() : __sprints_1HT,
        __sprints_2HT.name() : __sprints_2HT,
        __sprints_Forwards.name() : __sprints_Forwards,
        __sprints_Backwards.name() : __sprints_Backwards,
        __sprints_BallInPossesion.name() : __sprints_BallInPossesion,
        __sprints_BallNotInPossesion.name() : __sprints_BallNotInPossesion,
        __fastRuns.name() : __fastRuns,
        __fastRuns_Distance.name() : __fastRuns_Distance,
        __fastRuns_1HT.name() : __fastRuns_1HT,
        __fastRuns_2HT.name() : __fastRuns_2HT,
        __fastRuns_Forwards.name() : __fastRuns_Forwards,
        __fastRuns_Backwards.name() : __fastRuns_Backwards,
        __fastRuns_BallInPossesion.name() : __fastRuns_BallInPossesion,
        __fastRuns_BallNotInPossesion.name() : __fastRuns_BallNotInPossesion,
        __offensiveRuns.name() : __offensiveRuns,
        __offensiveRuns_Distance.name() : __offensiveRuns_Distance,
        __offensiveRuns_1HT.name() : __offensiveRuns_1HT,
        __offensiveRuns_2HT.name() : __offensiveRuns_2HT
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 307, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute avgDistance_Goalkeeper_EndLine uses Python identifier avgDistance_Goalkeeper_EndLine
    __avgDistance_Goalkeeper_EndLine = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_Goalkeeper_EndLine'), 'avgDistance_Goalkeeper_EndLine', '__AbsentNamespace0_CTD_ANON_23_avgDistance_Goalkeeper_EndLine', pyxb.binding.datatypes.float)
    __avgDistance_Goalkeeper_EndLine._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 310, 23)
    __avgDistance_Goalkeeper_EndLine._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 310, 23)
    
    avgDistance_Goalkeeper_EndLine = property(__avgDistance_Goalkeeper_EndLine.value, __avgDistance_Goalkeeper_EndLine.set, None, None)

    
    # Attribute avgDistance_Goalkeeper_EndLine_AtSaves uses Python identifier avgDistance_Goalkeeper_EndLine_AtSaves
    __avgDistance_Goalkeeper_EndLine_AtSaves = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avgDistance_Goalkeeper_EndLine_AtSaves'), 'avgDistance_Goalkeeper_EndLine_AtSaves', '__AbsentNamespace0_CTD_ANON_23_avgDistance_Goalkeeper_EndLine_AtSaves', pyxb.binding.datatypes.float)
    __avgDistance_Goalkeeper_EndLine_AtSaves._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 311, 23)
    __avgDistance_Goalkeeper_EndLine_AtSaves._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 311, 23)
    
    avgDistance_Goalkeeper_EndLine_AtSaves = property(__avgDistance_Goalkeeper_EndLine_AtSaves.value, __avgDistance_Goalkeeper_EndLine_AtSaves.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __avgDistance_Goalkeeper_EndLine.name() : __avgDistance_Goalkeeper_EndLine,
        __avgDistance_Goalkeeper_EndLine_AtSaves.name() : __avgDistance_Goalkeeper_EndLine_AtSaves
    })



sports_content = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sports-content'), CTD_ANON, documentation='Copyright (c) 2003 - 2011 proFILE Computersysteme GmbH.\n    All Rights Reserved.\n    proFILE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE SUITABILITY OF\n    THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE\n    IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE,\n    OR NON-INFRINGEMENT. proFILE SHALL NOT BE LIABLE FOR ANY DAMAGES SUFFERED\n    BY LICENSEE AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE\n    OR ITS DERIVATIVES.', location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 2, 1))
Namespace.addCategoryObject('elementBinding', sports_content.name().localName(), sports_content)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-metadata'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 15, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-event'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 27, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 15, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-event')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 27, 4))
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




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-title'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 18, 7)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-title')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 18, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'event-metadata'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 30, 7)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team'), CTD_ANON_4, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 45, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 45, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'event-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 30, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'team')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 45, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team-metadata'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 48, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'player'), CTD_ANON_7, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 66, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 66, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'team-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 48, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'player')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 66, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_3()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 51, 13)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 51, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_4()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'player-metadata'), CTD_ANON_8, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 69, 13)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'player-stats'), CTD_ANON_10, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 90, 13)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'player-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 69, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'player-stats')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 90, 13))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_5()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 72, 16)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 72, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_6()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rating'), CTD_ANON_11, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 93, 16)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'player-stats-soccer'), CTD_ANON_12, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 107, 16)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'player-stats-tracking'), CTD_ANON_16, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 185, 16)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 93, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 185, 16))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'rating')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 93, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'player-stats-soccer')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 107, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'player-stats-tracking')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 185, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_7()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-soccer-defensive'), CTD_ANON_13, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 110, 19)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-soccer-offensive'), CTD_ANON_14, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 123, 19)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-soccer-foul'), CTD_ANON_15, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 149, 19)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-soccer-defensive')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 110, 19))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-soccer-offensive')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 123, 19))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-soccer-foul')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 149, 19))
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
CTD_ANON_12._Automaton = _BuildAutomaton_8()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-time'), CTD_ANON_17, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 188, 19)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-ball'), CTD_ANON_18, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 199, 19)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-passes'), CTD_ANON_19, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 214, 19)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-duels'), CTD_ANON_20, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 238, 19)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-performance'), CTD_ANON_21, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 252, 19)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-runs'), CTD_ANON_22, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 278, 19)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stats-goalkeeper'), CTD_ANON_23, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 306, 19)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-time')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 188, 19))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-ball')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 199, 19))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-passes')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 214, 19))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-duels')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 238, 19))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-performance')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 252, 19))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-runs')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 278, 19))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'stats-goalkeeper')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/player_stats1.xsd', 306, 19))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_9()

