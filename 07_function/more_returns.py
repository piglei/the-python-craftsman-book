# -*- coding: utf-8 -*-


def user_get_tweets(user):
    """获取用户已发布状态

    - 如配置“展示随机状态”，获取随机状态
    - 如配置“不展示任何状态”，返回空的占位符状态
    - 默认返回最新状态
    """
    tweets = []
    if user.profile.show_random_tweets:
        tweets.extend(get_random_tweets(user))
    elif user.profile.hide_tweets:
        tweets.append(NULL_TWEET_PLACEHOLDER)
    else:
        # 最新状态需要用 token 从其他服务获取，并进行格式转换
        token = user.get_token()
        latest_tweets = get_latest_tweets(token)
        tweets.extend([transorm_tweet(item) for item in latest_tweets])
    return tweets


def user_get_tweets(user):
    """获取用户已发布状态"""
    if user.profile.show_random_tweets:
        return get_random_tweets(user)
    if user.profile.hide_tweets:
        return [NULL_TWEET_PLACEHOLDER]

    # 最新状态需要用 token 从其他服务获取，并进行格式转换
    token = user.get_token()
    latest_tweets = get_latest_tweets(token)
    return [transorm_tweet(item) for item in latest_tweets]