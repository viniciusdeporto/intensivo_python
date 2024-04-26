def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
    
user_profile = build_profile('vinicius', 'porto', location = 'araçatuba', campo = 'programação', idade=34, namorada = 'maiara')

print(user_profile)
    