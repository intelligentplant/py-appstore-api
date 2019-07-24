"""This module includes exmpale queries that can be made using the clients"""
__author__ = "Ross Kelso"
__docformat__ = 'reStructuredText'

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import intelligent_plant.utility as utility

def app_store_queries(app_store):
    """
    Tests the app store queries.
    :param app_store: An app store client instance.
    """
    #get the current users app store info
    print(app_store.get_user_info())

    #get the current users balance
    print(app_store.get_user_balance())

    #debit 1 credit from the account
    ref = app_store.debit_account(1)

    print(ref)

    #refund the transaction
    app_store.refund_account(ref)

def data_source(data_core):
    """
    Get all available data sources.
    :param data_core: A data core client instance
    :return: The available data sources
    """
    #get all datasource matching the filter "*" (so all of theme)
    return data_core.get_data_sources(["*"])

def tag_search(data_core, dsn):
    """
    Do a tag search
    :param data_core: A data core client instance
    :param dsn: The fully qualified name of a data source
    :return: The tags matching the search
    """
    #get the first page of tags from the provided data sourse fully qualified name
    return data_core.get_tags(dsn)[0]["Tags"]

def plot_tag(data_core, dsn, tag):
    """
    Plot the data for a specific tag.
    :param data_core: A data core client instance
    :param dsn: The fully qualified name of a data source
    :param tag: The name of the tag that should be plotted.
    """
    #request some data
    data = data_core.get_data(dsn, tag, "plot", "*-30d", "*", "1d")
    
    data_frame = utility.query_result_to_data_frame(data)

    #plot the data frame (plot.show should be called by the calling function)
    data_frame.plot(title="Single Tag")

def plot_tags(data_core, dsn, tag_names):
    """
    Plot the data for multiple tags
    :param data_core: A data core client instance
    :param dsn: The fully qualified name of a data source
    :param tags: The name of the tags that should be plotted.
    """
    #fetch the data for all the tags we found
    
    data = data_core.get_data(dsn, tag_names, "plot", "*-30d", "*", "1d")

    data_frame = utility.query_result_to_data_frame(data)
    
    #plot the data frame
    data_frame.plot(title="Lots of Data")

def snapshot(data_core, dsn, tag):
    """
    Get the snapshot value for a tag
    :param data_core: A data core client instance
    :param dsn: The fully qualified name of a data source
    :param tag: The name of the tag to query.
    """
    #do a snapshot query
    return data_core.get_data(dsn, tag, "now", points=1)