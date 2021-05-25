package com.zadanie.portlet;

import com.zadanie.constants.zadaniePortletKeys;

import java.io.IOException;

import com.liferay.portal.kernel.model.User;
import com.liferay.portal.kernel.portlet.bridges.mvc.MVCPortlet;
import com.liferay.portal.kernel.util.PortalUtil;

import javax.portlet.Portlet;
import javax.portlet.PortletException;
import javax.portlet.RenderRequest;
import javax.portlet.RenderResponse;

import org.osgi.service.component.annotations.Component;

/**
 * @author Dawid
 */
@Component(
	immediate = true,
	property = {
		"com.liferay.portlet.display-category=category.Zadanie",
		"com.liferay.portlet.header-portlet-css=/css/main.css",
		"com.liferay.portlet.instanceable=true",
		"javax.portlet.display-name=zadanie",
		"javax.portlet.init-param.template-path=/",
		"javax.portlet.init-param.view-template=/view.jsp",
		"javax.portlet.name=" + zadaniePortletKeys.ZADANIE,
		"javax.portlet.resource-bundle=content.Language",
		"javax.portlet.security-role-ref=power-user,user"
	},
	service = Portlet.class
)
public class zadaniePortlet extends MVCPortlet {
	@Override
	public void doView(RenderRequest renderRequest, RenderResponse renderResponse)
			throws IOException, PortletException {
		try {
			User user = PortalUtil.getUser(renderRequest);
			if (user != null) {
				renderRequest.getPreferences().setValue("check", "true");
				renderRequest.getPreferences().setValue("fullName", user.getFullName());
				renderRequest.getPreferences().setValue("email", user.getEmailAddress());
				renderRequest.getPreferences().setValue("ip", user.getLoginIP());
			} else {
				renderRequest.getPreferences().setValue("check", "false");
			}

		} catch (Throwable e) {
			e.printStackTrace();
		}
	super.doView(renderRequest, renderResponse);
		
	}
}