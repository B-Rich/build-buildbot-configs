# Additional branches that start as identical (individual variables can be overriden here)
PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    'accessibility': {
        'enable_nightly': True,
    },
    'build-system': {},
    'devtools':{
        'enable_nightly': True,
    },
    # Disabled because of builder limit problems - bug 721854
    #'electrolysis': {},
    'fx-team': {
        'repo_path': 'integration/fx-team',
        'enable_nightly': True,
    },
    # Turning off graphics - bug 649507
    #'graphics': {},
    'ionmonkey': {
        'enable_nightly': True
    },
    'jaegermonkey': {
        'enable_nightly': True
    },
    'mozilla-inbound': {
        'repo_path': 'integration/mozilla-inbound',
        'enable_perproduct_builds': True,
    },
    # Disabled because of builder limit problems - bug 721854
    #'places': {},
    # B2G builds not required on the profiling branch
    #'profiling': {},
    'services-central': {
        'repo_path': 'services/services-central'
    },
    # B2G builds not required on the UX branch
    #'ux': {
    #    'branch_name': 'UX',
    #    'mobile_branch_name': 'UX',
    #    'build_branch': 'UX',
    #    'enable_nightly': True,
    #},
    #####  TWIGS aka RENTABLE BRANCHES
    'alder': {},
    'ash': {},
    # Only need to build on OS X (testing gcc OS X builds still work)
    #'birch': {},
    'cedar': {},
    # Customizations for windows update service changes (bug 481815)
    #'elm': {},
    'holly': {},
    'larch': {},
    'maple': {},
    # Customizations for integration work for bugs 481815 and 307181
    'oak': {
        'enable_nightly': True
    },
    'pine': {},
}

# All is the default
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()