# Admin Manual

Generic overview of website architecture:

Website --(update via admin page)--> Google Sheets --(visiting ffactor.herokuapp.com/update)--> Caching Server --(webiste pulls all data from caching server)--> website

## Editing scores
1. Edit a score using the admin panel of the website
2. Edit a score directly in the google sheets, then visit ffactor.herokuapp.com/update to make the caching server update its scores, so that the updated scores can be seen on the website.

Note: as the master account (ffactor.master), you have the ability to change any of the cells in the google sheet. Do not update any cells OR sheet names outside of the scores or times of the given teams. Changing the content of other cells may break the website/caching server. The volunteer accounts (ffactor.volunteer/ffactor.backup) are restricted to only updating the acceptable cells on the site.

## Presenting The Winner
1. There is an html element prepared for you to make presenting the winner easy. to access it, you must use the website's wordpress admin interface. To do this, visit f.factor.skule.ca/wp-admin
2. log in with the given credentials
3. visit Pages > All pages > Home
4. click 'edit' on the top-most page element
5. there is a div tag at the very bottom of the first page element. remove the "style="display: none;" in it and edit the text appropriately
6. Click the preview button on the right to see what the changes will look like without actually updating the site.
7. When you are happy with the look of the site, click 'Update'. This will change the site!
6. Unhide the 'Overview' Sheet on the Public Google Sheet.

## Website Failure
In case of the website failure, use the Master-Public Google Sheets to communicate the scores to the students.