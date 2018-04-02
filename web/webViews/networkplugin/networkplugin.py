import json

from flask import session, render_template, redirect, request
from webViews.view import normalView
from webViews.dockletrequest import dockletRequest


class NetworkPluginView(normalView):
    template_path = 'networkplugin.html'

    @classmethod
    def get(cls):
        result = dockletRequest.post('/networkplugin/list/')
        # groups = dockletRequest.post('/user/groupNameList/')['groups']
        allnetworkplugins = result['networkplugins']
        return cls.render(cls.template_path, allnetworkplugins=allnetworkplugins)


class CreateNetworkPluginView(normalView):
    template_path = 'create_networkplugin.html'

    @classmethod
    def post(cls):
        dockletRequest.post('/networkplugin/create/', request.form)
        # return redirect('/admin/')
        return redirect('/networkplugin/')

# class QueryNotificationView(normalView):
#     template_path = 'notification_info.html'

#     @classmethod
#     def get_by_id(cls, notify_id):
#         notifies = []
#         if notify_id == 'all':
#             notifies.extend(dockletRequest.post('/notification/query/all/')['data'])
#         else:
#             notifies.append(dockletRequest.post('/notification/query/', data={'notify_id': notify_id})['data'])
#         return cls.render(cls.template_path, notifies=notifies)

class DeleteNetworkPluginView(normalView):
    @classmethod
    def post(cls):
        dockletRequest.post('/networkplugin/delete/', request.form)
        return redirect('/networkplugin/')
