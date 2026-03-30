import { chromium } from "playwright";

export async function captureRenderedPage(url) {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  try {
    await page.goto(url, {
      waitUntil: "networkidle",
      timeout: 60_000,
    });

    const html = await page.content();
    const title = await page.title();

    return {
      html,
      title,
      finalUrl: page.url(),
      fetchedAt: new Date().toISOString(),
    };
  } finally {
    await page.close();
    await browser.close();
  }
}
