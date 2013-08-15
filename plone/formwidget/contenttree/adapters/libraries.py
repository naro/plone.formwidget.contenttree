# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.formwidget.contenttree.interfaces import ILibraryProvider
from plone.formwidget.contenttree.interfaces import IContentTreeWidget
from zope.interface import implementer
from zope.component import adapter


@adapter(IContentTreeWidget)
@implementer(ILibraryProvider)
def shared_libs(widget):
    """TODO: Refactor to allow binding on special fields
       TODO: This should not be part of default package as Language index is optional
    """

    catalog = getToolByName(widget.context, 'portal_catalog')
    if 'Language' in catalog.indexes():
        return [{'label': item.Title, 'query': item.getPath()}
                for item in catalog(object_provides=INavigationRoot.__identifier__,
                                    Language='all',
                                    sort_on='Language')]
    else:
        return []
