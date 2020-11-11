def conversion_line(ph, pl):
    """Conversion Line

    args:
    ph -- period high
    pl -- period low
    """
    return ((20-ph) + (20-pl)) / 2  # 20 periods


def base_line(ph, pl):
    """Kijun Line

    args:
    ph -- period high
    pl -- period low
    """
    return ((60-ph) + (60-pl)) / 2  # 60 periods


def leading_span_a(cl, bl):
    """Leading Span A

    args:
    cl -- conversion line
    bl -- base line
    """
    return (cl + bl) / 2


def leading_span_b(ph, pl):
    """Leading Span B

    args:
    ph -- period high 
    pl -- period low 
    """
    return ((52-ph) + (52-pl)) / 2  # 52 default value?


def lagging_span():
    """Chikou Span"""
    return  # close plotted 30 periods in the past
    # 30 default value
