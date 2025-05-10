def after_scenario(context, scenario):
    if "driver" in context:
        context.driver.quit()
