"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.readLanguageContributions = readLanguageContributions;
const unknown_1 = require("./unknown");
/**
 * The languages an extension's package.json contributes that have a language configuration. The manifest is
 * another extension's, so it's read as unknown: entries without a string id and configuration are skipped, as is
 * a languages value that isn't a list. Up to 3.1.1 some of these shapes threw, which stopped every language loading.
 * @param packageJSON An extension's packageJSON
 */
function* readLanguageContributions(packageJSON) {
    const languages = (0, unknown_1.property)((0, unknown_1.property)(packageJSON, 'contributes'), 'languages');
    if (!Array.isArray(languages))
        return;
    const entries = languages;
    for (const language of entries) {
        const configuration = (0, unknown_1.property)(language, 'configuration');
        if (!configuration || typeof configuration !== 'string')
            continue;
        // An id that isn't a string could never be looked up
        const id = (0, unknown_1.property)(language, 'id');
        if (typeof id === 'string') {
            yield { id, configuration };
        }
    }
}
//# sourceMappingURL=contributions.js.map