# 仅当分组处于活跃状态时，允许用户加入分组并记录操作日志
if group.is_active:
    user = get_user_by_id(request.user_id)
    user.join(group)
    log_user_activiry(user, target=group, type=ActivityType.JOINED_GROUP)
else:
    user = get_user_by_id(request.user_id)
    log_user_activiry(user, target=group, type=ActivityType.JOIN_GROUP_FAILED)


user = get_user_by_id(request.user_id)

if group.is_active:
    user.join(group)
    activity_type = UserActivityType.JOINED_GROUP
else:
    activity_type = UserActivityType.JOIN_GROUP_FAILED

log_user_activiry(user, target=group, type=activity_type)


# 创建或更新用户资料数据
# 如果是新用户，创建新 Profile 数据，否则更新已有数据
if user.no_profile_exists:
    create_user_profile(
        username=data.username,
        gender=data.gender,
        email=data.email,
        age=data.age,
        address=data.address,
        points=0,
        created=now(),
    )
else:
    update_user_profile(
        username=data.username,
        gender=data.gender,
        email=data.email,
        age=data.age,
        address=data.address,
        updated=now(),
    )


if user.no_profile_exists:
    _update_or_create = create_user_profile
    extra_args = {'points': 0, 'created': now()}
else:
    _update_or_create = update_user_profile
    extra_args = {'updated': now()}

_update_or_create(
    username=user.username,
    gender=user.gender,
    email=user.email,
    age=user.age,
    address=user.address,
    **extra_args,
)