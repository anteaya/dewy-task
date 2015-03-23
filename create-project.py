#!/usr/bin/env python
# Copyright (c) 2015 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate configuration \
    to create a new project', add_help=True)

    parser.add_argument('new-project', action='store', help='the name of \
    the project you would like to add to Gerrit')

    subparsers = parser.add_subparsers(help='sub-command help')

    # Repo command - Name of new repo on which to grant Gerrit permissions
    repo_parser = subparsers.add_parser('repo-name', help='Name of project \
    upon which to change Gerrit permissions')
    repo_parser.add_argument('repo-name', action='store', help='Your \
    new project will be managed by Gerrit. This includes the \
    ability to merge code and create tags on your new repository. \
    Please state the name of the repository to allow new permissions to be \
    generated.')
    repo_parser.add_argument('--acl-file', action='store', help='You \
    have an acl file in Gerrit that you wish to use, state the namespace \
    and name of the file with extension ie. stackforege/puppet.config.')
    repo_parser.add_argument('--approve-group', action='store', help='You \
    want a Gerrit group to be able to +2 and Workflow +1 code other than \
    the generated default Gerrit group. State the group name of preference.')
    repo_parser.add_argument('--tagging-group', action='store', help='You \
    want a Gerrit group to be able to push tags on your repo other than the \
    generated default Gerrit group. State the group name of preference.')
    repo_parser.add_argument('--no-cla', action='store', help='You do not \
    want your contributors to have to sign the cla to contribute to your \
    repo.')

    # IRC command - Name of the IRC channel to add bot services
    irc_parser = subparsers.add_parser('irc-channel', help='Name of the \
    Freenode IRC channel you have registered & given infra permissions')
    irc_parser.add_argument('irc-channel', action='store', help='You \
    have registered a channel on freenode and granted permissions to \
    infra. State the channel name.')

    print parser.parse_args()

if __name__ == '__main__':
    main()
