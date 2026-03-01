def extract_url_features(url):
    """
    Extracts various features from a given URL.
    """
    features = {}

    # Extracting scheme (http or https)
    features['scheme'] = url.split('://')[0] if '://' in url else None

    # Extracting domain
    domain = url.split('://')[-1].split('/')[0]
    features['domain'] = domain

    # Extracting path
    path = '/'.join(url.split('://')[-1].split('/')[1:])
    features['path'] = path

    # Extracting query
    query_start = url.find('?')
    features['query'] = url[query_start + 1:] if query_start != -1 else None

    # Extracting fragment
    fragment_start = url.find('#')
    features['fragment'] = url[fragment_start + 1:] if fragment_start != -1 else None

    return features

def is_secure(url):
    """
    Checks if the given URL uses HTTPS.
    """ 
    return url.startswith('https://')

# Additional functions can be added as needed.