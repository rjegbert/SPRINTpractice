from tethys_sdk.base import TethysAppBase, url_map_maker


class Sprint(TethysAppBase):
    """
    Tethys app class for SPRINT.
    """

    name = 'SPRNT'
    index = 'sprint:home'
    icon = 'sprint/images/SPRINTLogo.JPG'
    package = 'sprint'
    root_url = 'sprint'
    color = '#3099fc'
    description = 'Simulation Program for River Networks'
    tags = ''
    enable_feedback = False
    feedback_emails = []


    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='sprint',
                controller='sprint.controllers.home'
            ),
            UrlMap(
                name='info',
                url='info',
                controller='sprint.controllers.info'
            ),
            UrlMap(
                name='map',
                url='map',
                controller='sprint.controllers.map'
            ),
            UrlMap(
                name='gizmo',
                url='gizmo',
                controller='sprint.controllers.gizmo'
            ),
            UrlMap(
                name='flow',
                url='flow',
                controller='sprint.controllers.flow'
            ),

        )

        return url_maps
