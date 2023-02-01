# -*- coding: utf-8 -*-


def sync_user_profile(user):
    # 同步用户资料到外部系统，仅当同步成功时发送通知消息
    sync_succeeded = False
    try:
        sync_profile(user.profile, to_external=True)
        sync_succeeded = True
    except Exception as e:
        print("Error while syncing user profile")

    if sync_succeeded:
        send_notification(user, 'profile sync succeeded')


def sync_user_profile(user):
    try:
        sync_profile(user.profile, to_external=True)
    except Exception as e:
        print("Error while syncing user profile")
    else:
        send_notification(user, 'profile sync succeeded')