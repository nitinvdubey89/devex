<?xml version="1.0" encoding="utf-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="exslt"><sch:ns uri="http://exslt.org/dynamic" prefix="dyn"/><sch:ns uri="http://markciecior.com/yang1" prefix="mc"/><sch:ns uri="urn:ietf:params:xml:ns:netconf:base:1.0" prefix="nc"/><sch:let name="root" value="/nc:data"/><sch:pattern id="ccdeve-candidate-module"><sch:rule context="/nc:data/mc:candidate/mc:certification"><sch:report test=". = preceding-sibling::mc:certification">Duplicate leaf-list entry "<sch:value-of select="."/>".</sch:report></sch:rule></sch:pattern></sch:schema>
