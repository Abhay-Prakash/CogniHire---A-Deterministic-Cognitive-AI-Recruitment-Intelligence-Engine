class AIRecruiterException(Exception):
    pass

class MalformedJSONError(AIRecruiterException):
    pass

class SchemaValidationError(AIRecruiterException):
    pass

class TimelineError(AIRecruiterException):
    pass

class HoneypotDetected(AIRecruiterException):
    pass

class ConfigurationError(AIRecruiterException):
    pass

class StreamingError(AIRecruiterException):
    pass
