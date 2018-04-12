import json

from flask import session, render_template, redirect, request
from webViews.view import normalView
from webViews.dockletrequest import dockletRequest


class NetworkPluginView(normalView):
    template_path = 'networkplugin.html'

    @classmethod
    def get(cls):
        masterips = dockletRequest.post_to_all()
        result = dockletRequest.post('/networkplugin/list/', {}, masterips[0].split("@")[0])
        # groups = dockletRequest.post('/user/groupNameList/')['groups']
        allnetworkplugins = result['networkplugins']
        return cls.render(cls.template_path, allnetworkplugins=allnetworkplugins)


class CreateNetworkPluginView(normalView):
    template_path = 'create_networkplugin.html'
    error_path = "error.html"

    @classmethod
    def post(self):
        masterips = dockletRequest.post_to_all()
        result = dockletRequest.post('/networkplugin/create/', request.form, masterips[0].split("@")[0])
        if(result.get('success', None) == "true"):
           return redirect("/networkplugin/")
        else:
            return self.render(self.error_path, message = result.get('message'))

class DeleteNetworkPluginView(normalView):
    error_path = "error.html"

    @classmethod
    def post(self):
        masterips = dockletRequest.post_to_all()
        result = dockletRequest.post('/networkplugin/delete/', request.form, masterips[0].split("@")[0])
        if(result.get('success', None) == "true"):
           return redirect("/networkplugin/")
            #return self.render(self.template_path, user = session['username'])
        else:
            return self.render(self.error_path, message = result.get('message'))
