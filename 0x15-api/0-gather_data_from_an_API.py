{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x15-api":{"items":[{"name":"0-gather_data_from_an_API.py","path":"0x15-api/0-gather_data_from_an_API.py","contentType":"file"},{"name":"1-export_to_CSV.py","path":"0x15-api/1-export_to_CSV.py","contentType":"file"},{"name":"2-export_to_JSON.py","path":"0x15-api/2-export_to_JSON.py","contentType":"file"},{"name":"3-dictionary_of_list_of_dictionaries.py","path":"0x15-api/3-dictionary_of_list_of_dictionaries.py","contentType":"file"},{"name":"README.md","path":"0x15-api/README.md","contentType":"file"}],"totalCount":5},"":{"items":[{"name":"0x00-shell_basics","path":"0x00-shell_basics","contentType":"directory"},{"name":"0x01-shell_permissions","path":"0x01-shell_permissions","contentType":"directory"},{"name":"0x02-shell_redirections","path":"0x02-shell_redirections","contentType":"directory"},{"name":"0x03-shell_variables_expansions","path":"0x03-shell_variables_expansions","contentType":"directory"},{"name":"0x04-loops_conditions_and_parsing","path":"0x04-loops_conditions_and_parsing","contentType":"directory"},{"name":"0x05-processes_and_signals","path":"0x05-processes_and_signals","contentType":"directory"},{"name":"0x06-regular_expressions","path":"0x06-regular_expressions","contentType":"directory"},{"name":"0x07-networking_basics","path":"0x07-networking_basics","contentType":"directory"},{"name":"0x08-networking_basics_2","path":"0x08-networking_basics_2","contentType":"directory"},{"name":"0x09-web_infrastructure_design","path":"0x09-web_infrastructure_design","contentType":"directory"},{"name":"0x0A-configuration_management","path":"0x0A-configuration_management","contentType":"directory"},{"name":"0x0B-ssh","path":"0x0B-ssh","contentType":"directory"},{"name":"0x0C-web_server","path":"0x0C-web_server","contentType":"directory"},{"name":"0x0D-web_stack_debugging_0","path":"0x0D-web_stack_debugging_0","contentType":"directory"},{"name":"0x0E-web_stack_debugging_1","path":"0x0E-web_stack_debugging_1","contentType":"directory"},{"name":"0x0F-load_balancer","path":"0x0F-load_balancer","contentType":"directory"},{"name":"0x10-https_ssl","path":"0x10-https_ssl","contentType":"directory"},{"name":"0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter","path":"0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter","contentType":"directory"},{"name":"0x12-web_stack_debugging_2","path":"0x12-web_stack_debugging_2","contentType":"directory"},{"name":"0x13-firewall","path":"0x13-firewall","contentType":"directory"},{"name":"0x14-mysql","path":"0x14-mysql","contentType":"directory"},{"name":"0x15-api","path":"0x15-api","contentType":"directory"},{"name":"attack_is_the_best_defense","path":"attack_is_the_best_defense","contentType":"directory"},{"name":"command_line_for_the_win","path":"command_line_for_the_win","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"lb-01","path":"lb-01","contentType":"file"},{"name":"web-01","path":"web-01","contentType":"file"},{"name":"web-02","path":"web-02","contentType":"file"}],"totalCount":28}},"fileTreeProcessingTime":5.702469,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":611280647,"defaultBranch":"master","name":"alx-system_engineering-devops","ownerLogin":"Blackhat-red-team","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-03-08T13:58:18.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/75793444?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1695483865.0","canEdit":false,"refType":"branch","currentOid":"05af47fa46aa1110532d53b6fd6a28982e28c9c7"},"path":"0x15-api/0-gather_data_from_an_API.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","\"\"\"retrieves information from a to-do list for a certain employee ID.\"\"\"","import requests","import sys","","if __name__ == \"__main__\":","    url = \"https://jsonplaceholder.typicode.com/\"","    client = requests.get(url + \"users/{}\".format(sys.argv[1])).json()","    todos = requests.get(url + \"todos\", params={\"userId\": sys.argv[1]}).json()","","    completed = [t.get(\"title\") for t in todos if t.get(\"completed\") is True]","    print(\"Employee {} is done with tasks({}/{}):\".format(","        client.get(\"name\"), len(completed), len(todos)))","    [print(\"\\t {}\".format(c)) for c in completed]"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":72,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":15,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-s"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":49,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":21,"cssClass":"pl-s1"},{"start":22,"end":25,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":42,"cssClass":"pl-s"},{"start":43,"end":49,"cssClass":"pl-en"},{"start":50,"end":53,"cssClass":"pl-s1"},{"start":54,"end":58,"cssClass":"pl-s1"},{"start":59,"end":60,"cssClass":"pl-c1"},{"start":64,"end":68,"cssClass":"pl-en"}],[{"start":4,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":20,"cssClass":"pl-s1"},{"start":21,"end":24,"cssClass":"pl-en"},{"start":25,"end":28,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":31,"end":38,"cssClass":"pl-s"},{"start":40,"end":46,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":48,"end":56,"cssClass":"pl-s"},{"start":58,"end":61,"cssClass":"pl-s1"},{"start":62,"end":66,"cssClass":"pl-s1"},{"start":67,"end":68,"cssClass":"pl-c1"},{"start":72,"end":76,"cssClass":"pl-en"}],[],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-s1"},{"start":19,"end":22,"cssClass":"pl-en"},{"start":23,"end":30,"cssClass":"pl-s"},{"start":32,"end":35,"cssClass":"pl-k"},{"start":36,"end":37,"cssClass":"pl-s1"},{"start":38,"end":40,"cssClass":"pl-c1"},{"start":41,"end":46,"cssClass":"pl-s1"},{"start":47,"end":49,"cssClass":"pl-k"},{"start":50,"end":51,"cssClass":"pl-s1"},{"start":52,"end":55,"cssClass":"pl-en"},{"start":56,"end":67,"cssClass":"pl-s"},{"start":69,"end":71,"cssClass":"pl-c1"},{"start":72,"end":76,"cssClass":"pl-c1"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":50,"cssClass":"pl-s"},{"start":51,"end":57,"cssClass":"pl-en"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":18,"cssClass":"pl-en"},{"start":19,"end":25,"cssClass":"pl-s"},{"start":28,"end":31,"cssClass":"pl-en"},{"start":32,"end":41,"cssClass":"pl-s1"},{"start":44,"end":47,"cssClass":"pl-en"},{"start":48,"end":53,"cssClass":"pl-s1"}],[{"start":5,"end":10,"cssClass":"pl-en"},{"start":11,"end":18,"cssClass":"pl-s"},{"start":12,"end":14,"cssClass":"pl-cce"},{"start":19,"end":25,"cssClass":"pl-en"},{"start":26,"end":27,"cssClass":"pl-s1"},{"start":30,"end":33,"cssClass":"pl-k"},{"start":34,"end":35,"cssClass":"pl-s1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":39,"end":48,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Blackhat-red-team/alx-system_engineering-devops/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/Blackhat-red-team/alx-system_engineering-devops/security/dependabot","repoSecurityAndAnalysisPath":"/Blackhat-red-team/alx-system_engineering-devops/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"0-gather_data_from_an_API.py","displayUrl":"https://github.com/Blackhat-red-team/alx-system_engineering-devops/blob/master/0x15-api/0-gather_data_from_an_API.py?raw=true","headerInfo":{"blobSize":"592 Bytes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"1e4aea3","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FBlackhat-red-team%2Falx-system_engineering-devops%2Fblob%2Fmaster%2F0x15-api%2F0-gather_data_from_an_API.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"14","truncatedSloc":"12"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/Blackhat-red-team/alx-system_engineering-devops/discussions/new","newIssuePath":"/Blackhat-red-team/alx-system_engineering-devops/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Blackhat-red-team/alx-system_engineering-devops/blob/master/0x15-api/0-gather_data_from_an_API.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/Blackhat-red-team/alx-system_engineering-devops/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/Blackhat-red-team/alx-system_engineering-devops/raw/master/0x15-api/0-gather_data_from_an_API.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Blackhat-red-team","repoName":"alx-system_engineering-devops","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Blackhat-red-team/alx-system_engineering-devops/branches":{"post":"JblFq6_6BCBitAqqZ_Cv57fcjIh-3HUDjiMlshuTgq_KARwMfwYcAVtC9eGE8A_QNYEcq1-kMrAyAVICsw6DcA"},"/repos/preferences":{"post":"JHGjB0zdJIkg7RcwhbbzZD5a3xHwp_zPpvnCv-lu6md_grXCPSyfW2JJ7STJvHiBPISHgL2Z4G3hDFEH6xCbbg"}}},"title":"alx-system_engineering-devops/0x15-api/0-gather_data_from_an_API.py at master · Blackhat-red-team/alx-system_engineering-devops"}