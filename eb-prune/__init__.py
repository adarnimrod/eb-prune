#!/usr/bin/env python
'''Prune older versions of an application in Elastic Beanstalk.'''
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from botocore import session


if __name__ == '__main__':
    print('Pruning Elastic Beanstalk versions.')
    session = session.get_session()
    beanstalk_client = session.create_client('elasticbeanstalk')
    response = beanstalk_client.describe_application_versions()
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise RuntimeError('Failed to describe application versions.')
    versions = response['ApplicationVersions']
    response = beanstalk_client.describe_environments()
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise RuntimeError('Failed to describe environments.')
    active_versions = [env['VersionLabel'] for env in response['Environments']]
    previous_versions = filter(
            lambda x: (not x['VersionLabel'] in active_versions) and
            x['Status'] == 'UNPROCESSED', versions)
    old_versions = sorted(previous_versions,
                          key=lambda x: x.get('DateCreated'))[:-400]
    for version in old_versions:
        response = beanstalk_client.delete_application_version(
                ApplicationName=version['ApplicationName'],
                VersionLabel=version['VersionLabel'],
                DeleteSourceBundle=True)
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise RuntimeError(
                    'Failed to delete version {0}.'.format(
                        version['VersionLabel']))
        print('Deleted version {0} of {1}.'.format(version['VersionLabel'],
              version['ApplicationName']))
    print('Deleted {0} versions.'.format(len(old_versions)))
