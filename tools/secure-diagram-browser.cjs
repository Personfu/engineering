"use strict";
const { assertPatchedVersion, secureBrowserExecutable } = require("../tests/security/browser-policy.cjs");
const puppeteer = require("puppeteer");

async function reviewedOptions() {
  const options = { executablePath: secureBrowserExecutable(), headless: true, args: [] };
  // Puppeteer's default sandbox stays enabled. Open no source files or URLs here.
  const browser = await puppeteer.launch(options);
  try {
    const version = await browser.version();
    assertPatchedVersion(version.replace(/^Chrome\//, ""));
    console.error(`Verified diagram renderer browser ${version}; sandbox enabled`);
  } finally {
    await browser.close();
  }
  return options;
}

if (require.main === module) {
  reviewedOptions().then((options) => {
    process.stdout.write(`${JSON.stringify(options)}\n`);
  }).catch(() => {
    console.error("Reviewed diagram browser unavailable or incompatible; no diagrams rendered.");
    process.exitCode = 1;
  });
}

module.exports = { reviewedOptions };
