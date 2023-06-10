"""Modify HTTP query and body param."""
from mitmproxy import http
import logging


def request(flow: http.HTTPFlow) -> None:
    
    #old_project = flow.request.query["project"]
    #new_project = old_project.replace("black_list_", "")
    #flow.request.query["cv"] = "2.1.3"
    old_did = flow.request.query["did"]
    new_did = old_did.replace("black_list_", "")
    flow.request.query["did"] = new_did
    old_content = flow.request.content
    new_content = old_content.replace(b"black_list_", b"")
    flow.request.content = new_content