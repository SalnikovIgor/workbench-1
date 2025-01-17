import { browser, protractor } from 'protractor';

import { AppPage } from './pages/home-page.po';
import { Helpers } from './pages/helpers';
import { Frameworks, TestUtils } from './pages/test-utils';
import { LoginPage } from './pages/login.po';
import { AnalyticsPopup } from './pages/analytics-popup.po';

describe('UI tests on Downloading Models', () => {
  let homePage: AppPage;
  let analyticsPopup: AnalyticsPopup;
  let protractorUntil;
  let helpers: Helpers;
  let testUtils: TestUtils;

  beforeAll(async () => {
    homePage = new AppPage();
    helpers = new Helpers();
    analyticsPopup = new AnalyticsPopup();
    protractorUntil = protractor.ExpectedConditions;
    testUtils = new TestUtils();
    await homePage.navigateTo();
    await browser.sleep(1000);
    await browser.refresh();
    await LoginPage.authWithTokenOnLoginPage();
    await analyticsPopup.refuseAnalyticsUsage();
  });

  beforeEach(async () => {
    await testUtils.testPreparation();
    await homePage.openConfigurationWizard();
  });

  it('list of models available for downloading is fetched', async () => {
    await testUtils.modelManagerPage.goToModelManager();
    await testUtils.modelManagerPage.openOMZTab();
    expect(browser.isElementPresent(testUtils.modelDownloadPage.modelDownloadTable)).toBeTruthy();
    expect(await testUtils.modelDownloadPage.downloadTableElementsCount()).toBeGreaterThan(0);
  });

  it('select model from table, download it and delete', async () => {
    const model = { name: 'squeezenet1.1', framework: Frameworks.CAFFE };
    const uploadedElementsCount = await testUtils.configurationWizard.uploadsModelsTableElementsCount();
    await testUtils.modelManagerPage.goToModelManager();
    await testUtils.modelManagerPage.openOMZTab();
    expect(await browser.isElementPresent(testUtils.modelDownloadPage.modelDownloadTable)).toBeTruthy();
    const modelName = await testUtils.modelDownloadPage.downloadModel(model.name);
    await testUtils.modelDownloadPage.convertDownloadedModelToIR();
    await testUtils.downloadAndDeleteModel(modelName, uploadedElementsCount);
  });

  it('Downloading IR model', async () => {
    const uploadedElementsCount = await testUtils.configurationWizard.uploadsModelsTableElementsCount();
    await testUtils.modelManagerPage.goToModelManager();
    await testUtils.modelManagerPage.openOMZTab();
    expect(await browser.isElementPresent(testUtils.modelDownloadPage.modelDownloadTable)).toBeTruthy();
    const modelName = await testUtils.modelDownloadPage.downloadModel('person-detection-retail-0013');
    await testUtils.downloadAndDeleteModel(modelName, uploadedElementsCount);
  });

  afterEach(async () => {
    await TestUtils.takeScreenshot();
    await TestUtils.getBrowserLogs();
  });
});
