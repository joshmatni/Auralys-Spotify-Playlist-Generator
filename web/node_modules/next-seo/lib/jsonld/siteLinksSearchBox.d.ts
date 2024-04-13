import React from 'react';
import { JsonLdProps } from './jsonld';
export interface PotentialAction {
    target: string;
    queryInput: string;
}
export interface SiteLinksSearchBoxJsonLdProps extends JsonLdProps {
    url: string;
    potentialActions: PotentialAction[];
}
declare function SiteLinksSearchBoxJsonLd({ type, keyOverride, potentialActions, ...rest }: SiteLinksSearchBoxJsonLdProps): React.JSX.Element;
export default SiteLinksSearchBoxJsonLd;
