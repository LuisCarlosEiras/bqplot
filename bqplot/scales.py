# Copyright 2015 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r"""

======
Scales
======

.. currentmodule:: bqplot.scales

.. autosummary::
   :toctree: generate/

   Scale
   LinearScale
   LogScale
   DateScale
   OrdinalScale
   ColorScale
   DateColorScale
   OrdinalColorScale

"""

from IPython.html.widgets import Widget
from IPython.utils.traitlets import Unicode, List, Enum, Float, Bool, Type

from .traits import Date


class Scale(Widget):

    """The base scale class

    Scale objects represent a mapping between data (the domain) and a visual quantity (The range).

    Attributes
    ----------
    domain_class: type
        type of the domain of the scale. Default value is float
    reverse: bool
        whether the scale should be reversed
    allow_padding: bool
        indicates whether figures are allowed to add data padding to this scale or not
    """
    domain_class = Type(Float, sync=False)
    reverse = Bool(False, sync=True)  #: Whether the scale should be reversed
    allow_padding = Bool(True, sync=True)  #: Boolean indicating if the figure should be able to add padding to the scale or not
    _view_name = Unicode('Scale', sync=True)
    _model_name = Unicode('ScaleModel', sync=True)
    _ipython_display_ = None  # We cannot display a scale outside of a figure


class LinearScale(Scale):

    """A linear scale

    An affine mapping from a numerical domain and a numerical range.

    Attributes
    ----------
    min: float (optional)
        if not None, min is the minimal value of the domain
    max: float (optional)
        if not None, max is the maximal value of the domain
    scale_range_type: string
        This attribute should not be modifed. The range type of a linear
        scale is numerical.
    """
    min = Float(default_value=None, sync=True, allow_none=True)
    max = Float(default_value=None, sync=True, allow_none=True)
    scale_range_type = Unicode('numerical', sync=True)
    _view_name = Unicode('LinearScale', sync=True)
    _model_name = Unicode('LinearScaleModel', sync=True)


class LogScale(Scale):

    """A log scale.

    A logarithmic mapping from a numerical domain to a numerical range.

    Attributes
    ----------
    min: float (optional)
        if not None, min is the minimal value of the domain
    max: float (optional)
        if not None, max is the maximal value of the domain
    scale_range_type: string
        This attribute should not be modifed by the user.
        The range type of a linear scale is numerical.
    """
    min = Float(default_value=None, sync=True, allow_none=True)
    max = Float(default_value=None, sync=True, allow_none=True)
    scale_range_type = Unicode('numerical', sync=True)
    _view_name = Unicode('LogScale', sync=True)
    _model_name = Unicode('LogScaleModel', sync=True)


class DateScale(Scale):

    """A date scale, with customizable formatting.

    An affine mapping from dates to a numerical range.

    Attributes
    ----------
    min: date (optional)
        if not None, min is the minimal value of the domain
    max: date (optional)
        if not None, max is the maximal value of the domain
    date_format: string
    scale_range_type: string
        This attribute should not be modifed by the user.
        The range type of a linear scale is numerical.
    """
    domain_class = Type(Date, sync=False)
    min = Date(default_value=None, sync=True, allow_none=True)
    max = Date(default_value=None, sync=True, allow_none=True)
    date_format = Unicode('', sync=True)
    scale_range_type = Unicode('numerical', sync=True)
    _view_name = Unicode('DateScale', sync=True)
    _model_name = Unicode('DateScaleModel', sync=True)


class OrdinalScale(Scale):

    """An ordinal scale.

    A mapping from a discrete set of values to a numerical range.

    Attributes
    ----------
    domain: list
        The discrete values mapped by the ordinal scale
    scale_range_type: string
        This attribute should not be modifed by the user.
        The range type of a linear scale is numerical.
    """
    domain = List(sync=True)
    scale_range_type = Unicode('numerical', sync=True)
    _view_name = Unicode('OrdinalScale', sync=True)
    _model_name = Unicode('OrdinalScaleModel', sync=True)


class ColorScale(Scale):

    """A color scale.

    A mapping from numbers to colors. The relation is affine by part.

    Attributes
    ----------
    scale_type: enum
    colors: list
    min: float
    max: float
    mid: float
    scheme: string
    scale_range_type: string
        This attribute should not be modifed by the user.
        The range type of a color scale is 'color'.
    """
    scale_type = Enum(['linear'], default_value='linear', sync=True)
    colors = List(sync=True)
    min = Float(default_value=None, sync=True, allow_none=True)
    max = Float(default_value=None, sync=True, allow_none=True)
    mid = Float(default_value=None, sync=True, allow_none=True)
    scheme = Unicode('RdYlGn', sync=True)
    scale_range_type = Unicode('Color', sync=True)
    _view_name = Unicode('LinearColorScale', sync=True)
    _model_name = Unicode('LinearColorScaleModel', sync=True)


class DateColorScale(ColorScale):

    """A date color scale.

    A mapping from dates to a numerical domain.

    Attributes
    ----------
    min: date
    max: date
    mid: date
    date_format: string
    scale_range_type: string
        This attribute should not be modifed by the user.
        The range type of a color scale is 'color'.
    """
    min = Date(default_value=None, sync=True, allow_none=True)
    max = Date(default_value=None, sync=True, allow_none=True)
    mid = Unicode(default_value=None, sync=True, allow_none=True)
    date_format = Unicode("", sync=True)
    scale_range_type = Unicode('Color', sync=True)
    _view_name = Unicode('DateColorScale', sync=True)
    _model_name = Unicode('DateColorScaleModel', sync=True)


class OrdinalColorScale(ColorScale):

    """An ordinal color scale.

    A mapping between a discrete set of value to colors.

    Attributes
    ----------
    domain: list
        The discrete values mapped by the ordinal scales.
    scale_range_type: string
        This attribute should not be modifed by the user.
        The range type of a color scale is 'color'.
    """
    domain = List(sync=True)
    scale_range_type = Unicode('Color', sync=True)
    _view_name = Unicode('OrdinalColorScale', sync=True)
    _model_name = Unicode('OrdinalScaleModel', sync=True)