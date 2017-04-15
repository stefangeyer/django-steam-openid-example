def user_details(user, details, strategy, *args, **kwargs):
    """Update user details using data from provider."""
    if user:
        changed = False  # flag to track changes
        protected = ('steamid', 'id', 'pk') + tuple(strategy.setting('PROTECTED_USER_FIELDS', []))

        # Update user model attributes with the new data sent by the current
        # provider. Update on some attributes is disabled by default, for
        # example username and id fields. It's also possible to disable update
        # on fields defined in SOCIAL_AUTH_PROTECTED_FIELDS.
        if details['player']:
            for name, value in details['player'].items():
                if value is not None and hasattr(user, name):
                    current_value = getattr(user, name, None)
                    if not current_value or name not in protected:
                        changed |= current_value != value
                        setattr(user, name, value)

        if changed:
            strategy.storage.user.changed(user)
