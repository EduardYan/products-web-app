"""
This module have the model
for the settings.
"""

class InvalidSetting(TypeError):
  """
  In case the setting passed for
  parameter is invalid.
  """
  pass

class Settings:
  """
  Model for the settings
  with properties.

  view_style for the view of products.

  """

  def __init__(self, view_style:str) -> None:
    if type(view_style) not in [str]:
      raise InvalidSetting('The view_style passed for parameter must be a string.')

    self.view_style = view_style
      